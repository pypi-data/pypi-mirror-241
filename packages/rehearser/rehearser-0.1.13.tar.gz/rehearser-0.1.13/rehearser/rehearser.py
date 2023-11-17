from typing import Any, Callable, Dict, List, Optional, Union
from unittest.mock import MagicMock, Mock
from rehearser.constants import RehearserType
from rehearser.mock_generator import MockGenerator
from rehearser.rehearser_method import RehearserMethod

from rehearser.rehearser_proxy import RehearserProxy

class Rehearser:
    def __init__(self, obj:Any=None, rehearser_type=None, interactions_src:Any=None) -> None:
        if obj:
            self._rehearser_type = RehearserType.INSTANCE
            if isinstance(obj, (Mock, MagicMock)):
                self._rehearser = RehearserProxy(obj)
            elif isinstance(obj, Callable):
                self._rehearser_type = RehearserType.METHOD
                self._rehearser = RehearserMethod(obj)
            else:
                self._rehearser = RehearserProxy(obj)
        else:
            if rehearser_type:
                self._rehearser_type = rehearser_type
        if interactions_src:
            self.load_interactions_src(interactions_src)
    
    def get_proxy(self):
        if self._rehearser_type == RehearserType.INSTANCE:
            return self._rehearser
        elif self._rehearser_type == RehearserType.METHOD:
            return self._rehearser.get_proxy_method()
        
    def get_interactions(self):
        return self._rehearser.get_interactions()
    
    def get_interactions_serializable_json(self):
        return self._rehearser.get_interactions_serializable_json()
    
    def get_interactions_file_path(self):
        return self._rehearser.get_interactions_file_path()
    
    def set_interactions_file_directory(self, directory: str):      
        self._rehearser.set_interactions_file_directory(directory)
        
    def set_entity_id(self, entity_id: str):
        self._rehearser.set_entity_id(entity_id)
        
    def set_scenario_name(self, scenario_name: str):
        self._rehearser.set_scenario_name(scenario_name)
        
    def set_use_timestamp(self, use_timestamp: bool):
        self._rehearser.set_use_timestamp(use_timestamp)

    def set_bucket_name(self, bucket_name: str):
        self._rehearser.set_bucket_name(bucket_name)
        
    def get_interactions_file_directory(self):
        return self._rehearser.get_interactions_file_directory()
    
    def get_entity_id(self):
        return self._rehearser.get_entity_id()
    
    def get_scenario_name(self):
        return self._rehearser.get_scenario_name()
    
    def get_use_timestamp(self):
        return self._rehearser.get_use_timestamp()
            
    def get_bucket_name(self):
        return self._rehearser.get_bucket_name()
        
    def write_interactions_to_file(self):
        self._rehearser.write_interactions_to_file()

    def write_interactions_to_s3(self):
        self._rehearser.write_interactions_to_s3()
        
    def load_interactions_src(self, interactions_src: Union[str, Dict[str, Any], List[Dict[str, Any]]]):
        if not hasattr(self, "_mock_generator"):
            self._mock_generator= MockGenerator(interactions_src=interactions_src)
        return self._mock_generator.load_interactions_src(interactions_src=interactions_src)
    
    def create_mock(self):
        if not hasattr(self, "_mock_generator"):
            self._mock_generator= MockGenerator(interactions_src=self.get_interactions())
        return self._mock_generator.create_mock()
                
