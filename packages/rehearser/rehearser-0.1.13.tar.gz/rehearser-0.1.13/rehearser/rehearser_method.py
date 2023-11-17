import datetime
import json
import os
from typing import Any, Callable, Dict, List, Optional
from unittest.mock import Mock
from rehearser.constants import GUMMIES_INTERACTIONS_FILE_TYPE, INTERACTIONS_KEY, INTERACTIONS_RAW_FILE_DEFAULT_DIRECTORY, InteractionType, RehearserType, SupportedInteractionsType
from rehearser.rehearser_mixin import RehearserMixin
from rehearser.utils import to_serializable_interactions

class RehearserMethod(RehearserMixin, object):
    def __init__(self, method: Callable):
        self._rehearser_type = RehearserType.METHOD
        self._obj=method      
        self._interactions: List[Dict[str, Any]] = []
        self._mock = Mock(side_effect=self._proxy_method)
        self._interactions_file_directory = None
        self._interactions_file_name = None
        self._interactions_file_path = None
        self._scenario_name = None
        self._entity_id = None
        self._use_timestamp = False
        self._bucket_name = None

    def _proxy_method(self, *args: Any, **kwargs: Any) -> Any:
        result = self._obj(*args, **kwargs)
        interaction = {
            "type": InteractionType.METHOD_CALL.name,
            "name": self._obj.__name__,
            "args": args,
            "kwargs": kwargs,
            "result": result,
        }
        self._interactions.append(interaction)
        return result

    def get_proxy_method(self):
        return self._mock

