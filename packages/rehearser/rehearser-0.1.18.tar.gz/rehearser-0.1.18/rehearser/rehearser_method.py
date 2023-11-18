import datetime
import json
import os
from typing import Any, Callable, Dict, List
from unittest.mock import Mock
from rehearser.constants import GUMMIES_INTERACTIONS_FILE_TYPE, INTERACTIONS_KEY, InteractionType, RehearserType, SupportedInteractionsType
from rehearser.rehearser_interactions_file_mixin import RehearserInteractionsFileMixin

class RehearserMethod(RehearserInteractionsFileMixin, object):
    def __init__(self, method: Callable):
        """
        RehearserMethod constructor.
        
        Args:
            method: The method to be rehearsed.    
        """
        RehearserInteractionsFileMixin.__init__(self)
        self.__obj=method      
        self.__interaction: List[Dict[str, Any]] = []

 
    def __call__(self, *args, **kwargs):
        interaction = {
            "type": InteractionType.METHOD_CALL.name,
            "name": self.__obj.__name__,
            "args": args,
            "kwargs": kwargs,
        }
        try:
            result = self.__obj(*args, **kwargs)
            interaction["result"] = result
            return result
        except Exception as e:
            interaction["exception"] = e
            raise
        finally:
            self.__interaction.append(interaction)


    def __enter__(self):
        interaction = {
            "type": InteractionType.METHOD_CALL.name,
            "name": "__enter__",
            "args": [],
            "kwargs": {},
        }
        try:
            result = self.__obj.__enter__()
            interaction["result"] = result
            return result
        except Exception as e:
            interaction["exception"] = e
            raise
        finally:
            self.__interaction.append(interaction)


    def __exit__(self, exc_type, exc_val, exc_tb):
        interaction = {
            "type": InteractionType.METHOD_CALL.name,
            "name": "__exit__",
            "args": [exc_type, exc_val, exc_tb],
            "kwargs": {},
        }
        try:
            result = self.__obj.__exit__(exc_type, exc_val, exc_tb)
            interaction["result"] = result
            return result
        except Exception as e:
            interaction["exception"] = e
            raise
        finally:
            self.__interaction.append(interaction)
 
    def get_interactions(self) -> Dict[str, Any]:
        """
        Get the interactions recorded so far.

        Returns:
            A dictionary of interactions.
        """
        return {
            GUMMIES_INTERACTIONS_FILE_TYPE: SupportedInteractionsType.PYTHON_CALLABLE.name,
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
        file_path_name += f"{self.__obj.__name__}/" if self.__obj.__name__ else ""
        file_path_name += f"{self.entity_id}/" if self.entity_id else ""
        if self.use_timestamp:
            file_path_name += f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S%f')}_interaction.json"
        else:
            file_path_name += self.interactions_file_name or "latest_interactions.json"      
        return file_path_name

    # def __side_effect_method(self, *args: Any, **kwargs: Any) -> Any:
    #     """
    #     A side effect method to be used by the mock. This method will record the interaction.
        
    #     Args: *args:Any, **kwargs: Any
        
    #     Returns:
    #         Any: The result of the method call.
    #     """
    #     interaction = {
    #         "type": InteractionType.METHOD_CALL.name,
    #         "name": self.__obj.__name__,
    #         "args": args,
    #         "kwargs": kwargs,
    #     }
    #     try:
    #         result = self.__obj(*args, **kwargs)
    #         interaction["result"] = result
    #         return result
    #     except Exception as e:
    #         interaction["exception"] = e
    #         raise
    #     finally:
    #         self.__interaction.append(interaction)

    # def get_proxy_method(self):
    #     """
    #         Get the proxy method.
    #     """
    #     return self.__mock

