import json
import os
from typing import Any, Callable, Dict, List, Optional
from unittest.mock import Mock, call

from rehearser.constants import (
    GUMMIES_INTERACTIONS_FILE_TYPE,
    INTERACTIONS_KEY,
    INTERACTIONS_RAW_FILE_DEFAULT_DIRECTORY,
    InteractionType,
    SupportedInteractionsType,
)
from rehearser.utils import to_serializable_interactions


class RehearserMethod:
    def __init__(self, method: Callable):
        self._method = method
        self._interactions: List[Dict[str, Any]] = []
        self._mock = Mock(side_effect=self._proxy_method)
        self._interactions_file_directory = None
        self._interactions_file_name = None
        self._interactions_file_path = None

    def _proxy_method(self, *args: Any, **kwargs: Any) -> Any:
        result = self._method(*args, **kwargs)
        interaction = {
            "type": InteractionType.METHOD_CALL.name,
            "name": self._method.__name__,
            "args": args,
            "kwargs": kwargs,
            "result": result,
        }
        self._interactions.append(interaction)
        return result

    def get_proxy_method(self):
        return self._mock

    def get_interactions(self) -> dict:
        """
        Get the interactions recorded so far.

        Returns:
            A list of interactions.
        """
        return {
            GUMMIES_INTERACTIONS_FILE_TYPE: SupportedInteractionsType.PYTHON_CALLABLE.name,
            INTERACTIONS_KEY: self._interactions,
        }

    def get_interactions_serializable_json(self) -> list[dict]:
        """
        Get the interactions recorded so far in serializable json format.

        Returns:
            A list of interactions in serializable json format.
        """
        return to_serializable_interactions(self.get_interactions())

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
            method_name = self._method.__name__
            directory += f"{method_name}/"
            filename = self._interactions_file_name or "latest_interactions.json"
            self._interactions_file_path = os.path.join(directory, filename)
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

    def set_interactions_file_directory(self, directory: str) -> None:
        """
        Set the directory of the interactions file.

        Args:
            directory: The directory of the interactions file.
        """
        self._interactions_file_directory = directory

    def get_interactions_file_directory(self) -> str:
        """
        Get the directory of the interactions file.

        Returns:
            The directory of the interactions file.
        """
        return self._interactions_file_directory
