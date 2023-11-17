import boto3
import datetime
import json
import os
from typing import Any, Dict, List, Optional, Union
from rehearser.constants import (
    GUMMIES_INTERACTIONS_FILE_TYPE,
    INTERACTIONS_KEY,
    INTERACTIONS_RAW_FILE_DEFAULT_DIRECTORY,
    SupportedInteractionsType,
    RehearserType,
)

from rehearser.utils import to_serializable_interactions


class RehearserInteractionsFileMixin(object):
    """
    A mixin class for recording interactions to a file.
    """
    def __init__(self) -> None:
        self.interactions_file_directory = None
        self.interactions_file_name = None
        self.interactions_file_dir_path_name = None
        self.scenario_name = None
        self.entity_id = None
        self.use_timestamp = False
        self.bucket_name = None
        
    def set_interactions_file_directory(self, interactions_file_directory: str) -> None:
        """
        Set the directory of the interactions file.

        Args:
            interactions_file_directory: The directory of the interactions file.
        """
        self.interactions_file_directory = interactions_file_directory


    def get_interactions_serializable_json(self) -> Dict[str, Any]:
        """
        Get the interactions recorded so far in serializable json format.

        Returns:
            A dictionary of serializable interactions.
        """
        return to_serializable_interactions(self.get_interactions())

    def get_interactions_file_dir_path_name(self) -> str:
        """
        Get the full path of the interactions file.

        Returns:
            The full path of the interactions file. (directory + filename)
        """
        if not self.interactions_file_dir_path_name:
            directory = (
                self.interactions_file_directory
                or INTERACTIONS_RAW_FILE_DEFAULT_DIRECTORY
            )
            directory += "/" if directory[-1] != "/" else ""
            return os.path.join(directory, self.get_file_path_name())

        return self.interactions_file_dir_path_name        

    def write_interactions_to_file(self, file_dir_path_name: Optional[str] = None) -> None:
        """
        Save the interactions recorded so far to a file.

        Args:
            file_path: The path of the file to write the interactions to.
        """
        if file_dir_path_name:
            self.interactions_file_dir_path_name = file_dir_path_name
        else:
            file_dir_path_name = self.get_interactions_file_dir_path_name()
        doc_str = json.dumps(self.get_interactions_serializable_json(), indent=2)
        print(f"Writing interactions to file: {file_dir_path_name}, with {len(doc_str)} chars")
        directory = os.path.dirname(file_dir_path_name)
        os.makedirs(directory, exist_ok=True)
        with open(file_dir_path_name, "w") as f:
            f.write(doc_str)


    def write_interactions_to_s3(self, bucket_name: Optional[str]=None, s3_key: Optional[str]=None):
        """
        Save the interactions to an S3 bucket.

        Args:
            bucket_name: The name of the S3 bucket.
            s3_key: The key of the file in the S3 bucket.
        """
        if bucket_name is None:
            bucket_name = self.getbucket_name()
        if s3_key is None:
            s3_key = self.get_filename_path()
        s3 = boto3.resource('s3')
        interactions = self.get_interactions_serializable_json()
        interactions_json = json.dumps(interactions, indent=2)
        print(
            f"Uploading interactions to S3 bucket: {bucket_name}, key: {s3_key}, with {len(interactions_json)} chars"
        )
        s3.Object(bucket_name, s3_key).put(Body=interactions_json)
