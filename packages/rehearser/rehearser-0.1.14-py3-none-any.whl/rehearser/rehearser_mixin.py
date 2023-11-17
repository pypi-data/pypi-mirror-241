import boto3
import datetime
import json
import os
from typing import Any, Dict, List, Optional, Union
from rehearser.constants import (
    GUMMIES_INTERACTIONS_FILE_TYPE,
    INTERACTIONS_KEY,
    INTERACTIONS_RAW_FILE_DEFAULT_DIRECTORY,
    InteractionType,
    SupportedInteractionsType,
    RehearserType,
)

from rehearser.utils import to_serializable_interactions


class RehearserMixin(object):
    def get_interactions(self) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        """
        Get the interactions recorded so far.

        Returns:
            A list of interactions.
        """
        return {
            GUMMIES_INTERACTIONS_FILE_TYPE: {
                RehearserType.INSTANCE: SupportedInteractionsType.PYTHON_INSTANCE.name,
                RehearserType.METHOD: SupportedInteractionsType.PYTHON_CALLABLE.name,
            }.get(self._rehearser_type),
            INTERACTIONS_KEY: self._interactions,
        }

    def get_interactions_file_directory(self) -> str:
        """
        Get the directory of the interactions file.

        Returns:
            The directory of the interactions file.
        """
        return self._interactions_file_directory

    def set_interactions_file_directory(self, directory: str) -> None:
        """
        Set the directory of the interactions file.

        Args:
            directory: The directory of the interactions file.
        """
        self._interactions_file_directory = directory

    def get_entity_id(self) -> str:
        """
        Get the entity id of the interactions file.

        Returns:
            The entity id of the interactions file.
        """
        return self._entity_id

    def set_entity_id(self, entity_id: str) -> None:
        """
        Set the entity id of the interactions file.

        Args:
            entity_id: The entity id of the interactions file.
        """
        self._entity_id = entity_id

    def get_scenario_name(self) -> str:
        """
        Get the scenario name of the interactions file.

        Returns:
            The scenario name of the interactions file.
        """
        return self._scenario_name

    def set_scenario_name(self, scenario_name: str) -> None:
        """
        Set the scenario name of the interactions file.

        Args:
            scenario_name: The scenario name of the interactions file.
        """
        self._scenario_name = scenario_name

    def get_use_timestamp(self) -> bool:
        """
        Get the use timestamp of the interactions file.

        Returns:
            The use timestamp of the interactions file.
        """
        return self._use_timestamp

    def set_use_timestamp(self, use_timestamp: bool) -> None:
        """
        Set the use timestamp of the interactions file.

        Args:
            use_timestamp: The use timestamp of the interactions file.
        """
        self._use_timestamp = use_timestamp

    def get_bucket_name(self) -> str:
        """
        Get the bucket name of the interactions file.

        Returns:
            The bucket name of the interactions file.
        """
        return self._bucket_name
    
    def set_bucket_name(self, bucket_name: str) -> None:
        """
        Set the bucket name of the interactions file.

        Args:
            bucket_name: The bucket name of the interactions file.
        """
        self._bucket_name = bucket_name
        
    def get_interactions_serializable_json(self) -> list[dict]:
        """
        Get the interactions recorded so far in serializable json format.

        Returns:
            A list of interactions in serializable json format.
        """
        return to_serializable_interactions(self.get_interactions())

    def get_filename_path(self) -> str:
        """
        Get the filename path of the interactions file.
        """
        filenamepath = ""
        filenamepath += f"{self._scenario_name}/" if self._scenario_name else ""
        component_name = (
            self._obj.__name__
            if self._rehearser_type == RehearserType.METHOD
            else self._obj.__class__.__name__
        )
        filenamepath += f"{component_name}/" if component_name else ""
        filenamepath += f"{self._entity_id}/" if self._entity_id else ""
        if self._use_timestamp:
            filenamepath += f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S%f')}_interactions.json"
        else:
            filenamepath += self._interactions_file_name or "latest_interactions.json"      
        return filenamepath

    def get_interactions_file_path(self) -> str:
        """
        Get the path of the interactions file.

        Returns:
            The path of the interactions file.
        """
        if not self._interactions_file_path:
            directory = (
                self._interactions_file_directory
                or INTERACTIONS_RAW_FILE_DEFAULT_DIRECTORY
            )
            directory += "/" if directory[-1] != "/" else ""
            filename_path = self.get_filename_path()
            return os.path.join(directory, filename_path)

        return self._interactions_file_path

    def write_interactions_to_file(self, file_path: Optional[str] = None) -> None:
        """
        Write the interactions recorded so far to a file.

        Args:
            file_path: The path of the file to write the interactions to.
        """
        if file_path:
            self._interactions_file_path = file_path
        else:
            file_path = self.get_interactions_file_path()
        doc_str = json.dumps(self.get_interactions_serializable_json(), indent=2)
        print(f"Writing interactions to file: {file_path}, with {len(doc_str)} chars")
        directory = os.path.dirname(file_path)
        os.makedirs(directory, exist_ok=True)
        with open(file_path, "w") as f:
            f.write(doc_str)


    def write_interactions_to_s3(self, bucket_name: Optional[str]=None, s3_key: Optional[str]=None):
        """
        Save the interactions to an S3 bucket.

        Args:
            bucket_name: The name of the S3 bucket.
            s3_key: The key of the file in the S3 bucket.
        """
        if bucket_name is None:
            bucket_name = self.get_bucket_name()
        if s3_key is None:
            s3_key = self.get_filename_path()
        s3 = boto3.resource('s3')
        interactions = self.get_interactions_serializable_json()
        interactions_json = json.dumps(interactions, indent=2)
        print(
            f"Uploading interactions to S3 bucket: {bucket_name}, key: {s3_key}, with {len(interactions_json)} chars"
        )
        s3.Object(bucket_name, s3_key).put(Body=interactions_json)
