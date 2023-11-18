from typing import Any, Callable, Dict, List, Union
from unittest.mock import MagicMock, Mock
from rehearser.constants import RehearserType
from rehearser.mock_generator import MockGenerator
from rehearser.rehearser_method import RehearserMethod

from rehearser.rehearser_proxy import RehearserProxy

class Rehearser:
    def __init__(self, obj:Any=None, rehearser_type=None, interactions_src:Any=None) -> None:
        if obj:
            self.__rehearser_type = RehearserType.INSTANCE
            if isinstance(obj, (Mock, MagicMock)):
                self.__rehearser = RehearserProxy(obj)
            elif isinstance(obj, Callable):
                self.__rehearser_type = RehearserType.METHOD
                self.__rehearser = RehearserMethod(obj)
            else:
                self.__rehearser = RehearserProxy(obj)
        else:
            if rehearser_type:
                self.__rehearser_type = rehearser_type
        print(self.__rehearser_type.name)
        if interactions_src:
            self.load_interactions_src(interactions_src)
    
    def get_proxy(self) -> Any:
        return self.__rehearser
        
    def get_interactions(self) -> Dict[str, Any]:
        return self.__rehearser.get_interactions()
    
    def get_interactions_serializable_json(self) -> Dict[str, Any]:
        return self.__rehearser.get_interactions_serializable_json()

    @property    
    def interactions_file_directory(self) -> str:
        return self.__rehearser.interactions_file_directory()

    @interactions_file_directory.setter     
    def interactions_file_directory(self, interactions_file_directory: str) -> None:      
        self.__rehearser.interactions_file_directory = interactions_file_directory

    @property    
    def scenario_name(self) -> str:
        return self.__rehearser.scenario_name()

    @scenario_name.setter     
    def scenario_name(self, scenario_name: str) -> None:      
        self.__rehearser.scenario_name = scenario_name

    @property    
    def entity_id(self) -> str:
        return self.__rehearser.entity_id()

    @scenario_name.setter     
    def entity_id(self, entity_id: str) -> None:      
        self.__rehearser.entity_id = entity_id

    @property    
    def use_timestamp(self) -> str:
        return self.__rehearser.use_timestamp

    @use_timestamp.setter     
    def use_timestamp(self, use_timestamp: str) -> None:      
        self.__rehearser.use_timestamp = use_timestamp

    @property    
    def bucket_name(self) -> str:
        return self.__rehearser.bucket_name

    @bucket_name.setter     
    def bucket_name(self, bucket_name: str) -> None:      
        self.__rehearser.bucket_name = bucket_name


    def set_interactions_file_directory(self, interactions_file_directory: str) -> None:
        return self.__rehearser.set_interactions_file_directory(interactions_file_directory)

    def get_finalized_interactions_file_dir_path_name(self) -> str:
        return self.__rehearser.get_finalized_interactions_file_dir_path_name()
        
    def get_file_path_name(self) -> str:
        return self.__rehearser.get_file_path_name()
    
    def write_interactions_to_file(self):
        self.__rehearser.write_interactions_to_file()

    def write_interactions_to_s3(self):
        self.__rehearser.write_interactions_to_s3()
        
    def load_interactions_src(self, interactions_src: Union[str, Dict[str, Any], List[Dict[str, Any]]]):
        if not hasattr(self, "_mock_generator"):
            self._mock_generator= MockGenerator(interactions_src=interactions_src)
        return self._mock_generator.load_interactions_src(interactions_src=interactions_src)
    
    def create_mock(self):
        if not hasattr(self, "_mock_generator"):
            self._mock_generator= MockGenerator(interactions_src=self.get_interactions())
        return self._mock_generator.create_mock()
                
