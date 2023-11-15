import json
import os
from typing import Any, Optional

from rehearser.constants import INTERACTIONS_RAW_FILE_DEFAULT_DIRECTORY, InteractionType
from rehearser.utils import to_serializable_interactions


class RehearserProxy:
    """
    A proxy class that records all interactions with the proxied object.
    """

    def __init__(self, obj: Any) -> None:
        """
        Initialize a RehearserProxy object.

        Args:
            obj: The object to be proxied.
        """
        self._interactions_file_directory = None
        self._interactions_file_name = None
        self._interactions_file_path = None
        self._obj = obj
        self._interactions = []
        ## Record initial state of a obj
        for attr_name in obj.__dict__.keys():
            if attr_name not in [
                "_obj",
                "_interactions",
                "_interactions_file_directory",
                "_interactions_file_name",
                "_interactions_file_path",
            ]:
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
        if name in [
            "_obj",
            "_interactions",
            "_interactions_file_directory",
            "_interactions_file_name",
            "_interactions_file_path",
        ]:
            super().__setattr__(name, value)
        else:
            self._interactions.append(
                {
                    "type": InteractionType.ATTRIBUTE_ASSIGNMENT.name,
                    "name": name,
                    "value": value,
                }
            )
            setattr(self._obj, name, value)

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

    def get_interactions(self) -> list[dict]:
        """
        Get the interactions recorded so far.

        Returns:
            A list of interactions.
        """
        return self._interactions

    def get_interactions_serializable_json(self) -> list[dict]:
        """
        Get the interactions recorded so far in serializable json format.

        Returns:
            A list of interactions in serializable json format.
        """
        return to_serializable_interactions(self._interactions)

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
            class_name = self._obj.__class__.__name__
            directory += f"{class_name}/"
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
