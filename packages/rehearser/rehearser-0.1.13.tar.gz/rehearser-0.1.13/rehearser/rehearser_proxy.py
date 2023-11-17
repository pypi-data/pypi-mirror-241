import datetime
import json
import os
from typing import Any, Dict, List, Optional, Union

from rehearser.constants import FILTERED_ATTRS, GUMMIES_INTERACTIONS_FILE_TYPE, INTERACTIONS_KEY, INTERACTIONS_RAW_FILE_DEFAULT_DIRECTORY, InteractionType, RehearserType, SupportedInteractionsType
from rehearser.rehearser_mixin import RehearserMixin
from rehearser.utils import to_serializable_interactions

class RehearserProxy(RehearserMixin, object):
    """
    A proxy class that records all interactions with the proxied object.
    """

    def __init__(self, obj: Any) -> None:
        """
        Initialize a RehearserProxy object.

        Args:
            obj: The object to be proxied.
        """
        self._rehearser_type = RehearserType.INSTANCE
        self._obj = obj              
        self._interactions = []
        self._interactions_file_directory = None
        self._interactions_file_name = None
        self._interactions_file_path = None
        self._scenario_name = None
        self._entity_id = None
        self._use_timestamp = False
        self._bucket_name = None
        ## Record initial state of a obj
        for attr_name in obj.__dict__.keys():
            if attr_name not in FILTERED_ATTRS:
                self._interactions.append(
                    {
                        "type": InteractionType.INITIAL.name,
                        "name": attr_name,
                        "result": getattr(obj, attr_name),
                    }
                )

    def __getattr__(self, name: str) -> Any:
        """
        Override the __getattr__ method to record interactions.

        Args:
            name: The name of the attribute being accessed.

        Returns:
            A wrapper function that records the interaction and then calls the original method.
        """
        # print(f"[temp_debug][RehearserProxy]Triggered!! {name}")
        attr = getattr(self._obj, name)
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
                    self._interactions.append(interaction)

            return wrapper
        else:
            value = getattr(self._obj, name)
            self._interactions.append(
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
        if name not in FILTERED_ATTRS:
            self._interactions.append(
                {
                    "type": InteractionType.ATTRIBUTE_ASSIGNMENT.name,
                    "name": name,
                    "value": value,
                }
            )
            setattr(self._obj, name, value)
        else:
            super().__setattr__(name, value)

    def __delattr__(self, name: str) -> None:
        """
        Override the __delattr__ method to record interactions.

        Args:
            name: The name of the attribute being deleted.
        """
        self._interactions.append(
            {"type": InteractionType.ATTRIBUTE_DELETION.name, "name": name}
        )
        delattr(self._obj, name)
  
