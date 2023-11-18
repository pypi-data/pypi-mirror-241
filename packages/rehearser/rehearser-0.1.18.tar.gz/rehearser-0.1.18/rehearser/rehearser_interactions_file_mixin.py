import boto3
import json
import os
from typing import Any, Dict, Optional
from rehearser.constants import (
    INTERACTIONS_KEY,
    INTERACTIONS_RAW_FILE_DEFAULT_DIRECTORY,
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

    def get_finalized_interactions_file_dir_path_name(self) -> str:
        """
        Calculate the finalized full path of the interactions file based on
        these attributes:
        - interactions_file_dir_path_name (considered first)
        - interactions_file_directory
        - interactions_file_name

        Returns:
            The full path of the interactions file. (directory + filename)
        """
        if self.interactions_file_dir_path_name:
            return self.interactions_file_dir_path_name        
        else:
            directory = (
                self.interactions_file_directory
                or INTERACTIONS_RAW_FILE_DEFAULT_DIRECTORY
            )
            directory += "/" if directory[-1] != "/" else ""
            return os.path.join(directory, self.get_file_path_name())


    def write_interactions_to_file(self, file_dir_path_name: Optional[str] = None) -> None:
        """
        Save the interactions recorded so far to a file.

        Args:
            file_path: The path of the file to write the interactions to.
        """
        if file_dir_path_name:
            self.interactions_file_dir_path_name = file_dir_path_name
        
        final_file_dir_path_name = self.get_finalized_interactions_file_dir_path_name()
        doc_str = json.dumps(self.get_interactions_serializable_json(), indent=2)
        print(f"Writing interactions to file: {final_file_dir_path_name}, with {len(doc_str)} chars")
        directory = os.path.dirname(final_file_dir_path_name)
        os.makedirs(directory, exist_ok=True)
        with open(final_file_dir_path_name, "w") as f:
            f.write(doc_str)

    def load_interactions_from_file(self, filename: str, append: Optional[bool]=False):
        """
        Load the interactions from a file.

        Args:
            filename: The name of the file.
            append: Whether to append the loaded interactions to the existing ones.
        """
        with open(filename, 'r') as f:
            try:
                interactions_json = json.load(f)
            except json.decoder.JSONDecodeError as e:
                print(f"Error loading interactions from file: {filename}")
                raise e
            except Exception as e:
                print(f"Error loading interactions from file: {filename}")
                raise e
            if isinstance(interactions_json, dict):
                interactions = interactions_json.get(INTERACTIONS_KEY, [])
            elif isinstance(interactions_json, list):
                interactions = interactions_json
        if append:
            self.__interactions.extend(interactions)
        else:
            self.__interactions = interactions
        
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
