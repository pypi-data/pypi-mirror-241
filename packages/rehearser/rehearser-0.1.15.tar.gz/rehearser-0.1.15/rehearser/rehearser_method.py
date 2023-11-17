import datetime
import json
import os
from typing import Any, Callable, Dict, List
from unittest.mock import Mock
from rehearser.constants import InteractionType, RehearserType
from rehearser.rehearser_interactions_file_mixin import RehearserInteractionsFileMixin

class RehearserMethod(RehearserInteractionsFileMixin, object):
    def __init__(self, method: Callable):
        self._rehearser_type = RehearserType.METHOD
        self._obj=method      
        self._interactions: List[Dict[str, Any]] = []
        self._mock = Mock(side_effect=self._proxy_method)
        RehearserInteractionsFileMixin.__init__(self)
 

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

