import datetime
from typing import Any, Dict, List

from rehearser.constants import GUMMIES_INTERACTIONS_FILE_TYPE, INTERACTIONS_KEY, REHEARSER_PROXY_FILTERED_ATTRS, InteractionType, RehearserType, SupportedInteractionsType
from rehearser.rehearser_interactions_file_mixin import RehearserInteractionsFileMixin

class RehearserProxy(RehearserInteractionsFileMixin, object):
    """
    A proxy class that records all interactions with the proxied object.
    """

    setter_filtered_name = REHEARSER_PROXY_FILTERED_ATTRS + [f"_RehearserProxy{name}" for name in REHEARSER_PROXY_FILTERED_ATTRS]

    def __init__(self, obj: Any) -> None:
        """
        Initialize a RehearserProxy object.

        Args:
            obj: The object to be proxied.
        """
        RehearserInteractionsFileMixin.__init__(self)
        self.__obj = obj              
        self.__interaction: List[Dict[str, Any]] = []
        
        ## Record initial state of a obj
        for attr_name in obj.__dict__.keys():
            if attr_name not in REHEARSER_PROXY_FILTERED_ATTRS:
                self.__interaction.append(
                    {
                        "type": InteractionType.INITIAL.name,
                        "name": attr_name,
                        "result": getattr(obj, attr_name),
                    }
                )

    def get_interactions(self) -> Dict[str, Any]:
        """
        Get the interactions recorded so far.

        Returns:
            A dictionary of interactions.
        """
        return {
            GUMMIES_INTERACTIONS_FILE_TYPE: SupportedInteractionsType.PYTHON_INSTANCE.name,
            INTERACTIONS_KEY: self.__interaction,
        }

    def get_file_path_name(self) -> str:
        """
        Get the filepath and filename of the interactions file.
        
        Returns:
            The filepath and filename of the interactions file.
        """
        file_path_name = ""
        file_path_name += f"{self.scenario_name}/" if self.scenario_name else ""
        file_path_name += f"{self.__obj.__class__.__name__}/" if self.__obj.__class__.__name__ else ""
        file_path_name += f"{self.entity_id}/" if self.entity_id else ""
        if self.use_timestamp:
            file_path_name += f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S%f')}__interaction.json"
        else:
            file_path_name += self.interactions_file_name or "latest_interactions.json"      
        return file_path_name

    def __getattr__(self, name: str) -> Any:
        """
        Override the __getattr__ method to record interactions.

        Args:
            name: The name of the attribute being accessed.

        Returns:
            A wrapper function that records the interaction and then calls the original method.
        """
        attr = getattr(self.__obj, name)
        if callable(attr):

            def wrapper(*args, **kwargs):
                interaction = {
                    "type": InteractionType.INSTANCE_METHOD_CALL.name,
                    "name": name,
                    "args": args,
                    "kwargs": kwargs,
                }
                try:
                    result = attr(*args, **kwargs)
                    interaction["result"] = result
                    return result
                except Exception as e:
                    interaction["exception"] = e
                    raise
                finally:
                    self.__interaction.append(interaction)

            return wrapper
        else:
            value = getattr(self.__obj, name)
            self.__interaction.append(
                {
                    "type": InteractionType.ATTRIBUTE_ACCESS.name,
                    "name": name,
                    "result": value,
                }
            )
            return value

    def __setattr__(self, name: str, value: Any) -> None:
        """
        Override the __setattr__ method to record interactions.

        Args:
            name: The name of the attribute being set.
            value: The value being assigned to the attribute.
        """
        if name not in RehearserProxy.setter_filtered_name:
            print(f"[temp_debug] __setattr__ {name} {value}")
            self.__interaction.append(
                {
                    "type": InteractionType.ATTRIBUTE_ASSIGNMENT.name,
                    "name": name,
                    "value": value,
                }
            )
            setattr(self.__obj, name, value)
        else:
            super().__setattr__(name, value)

    def __delattr__(self, name: str) -> None:
        """
        Override the __delattr__ method to record interactions.

        Args:
            name: The name of the attribute being deleted.
        """
        self.__interaction.append(
            {"type": InteractionType.ATTRIBUTE_DELETION.name, "name": name}
        )
        delattr(self.__obj, name)
  
