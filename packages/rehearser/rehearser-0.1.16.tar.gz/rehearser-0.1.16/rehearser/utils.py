import json
import os
from typing import Any, Dict, Union
from unittest.mock import Mock

from rehearser.constants import GUMMIES_TYPE


def serialize_exception(e: Exception) -> str:
    """
    Serialize an exception into a JSON string.

    Args:
        e: The exception to be serialized.

    Returns:
        The serialized exception as a JSON string.
    """
    return json.dumps({"type": type(e).__name__, "message": str(e)})


def deserialize_exception(serialized_exception: str) -> Exception:
    """
    Deserialize a JSON string into an exception.

    Args:
        serialized_exception: The serialized exception as a JSON string.

    Returns:
        The deserialized exception.
    """
    exception_dict = json.loads(serialized_exception)
    # Dynamically create an exception of the correct type with the same message
    return eval(exception_dict["type"])(exception_dict["message"])


def to_serializable_interactions(obj):
    """
    Convert a object back to a serializable object form

    Args:
        obj: The object to be converted.

    Returns:
        The converted object.
    """
    if isinstance(obj, (int, float, str, bool, type(None))):
        return obj
    if isinstance(obj, list):
        return [to_serializable_interactions(item) for item in obj]
    if isinstance(obj, set):
        return {to_serializable_interactions(item) for item in obj}
    if isinstance(obj, tuple):
        return tuple(to_serializable_interactions(item) for item in obj)
    if isinstance(obj, dict):
        return {key: to_serializable_interactions(value) for key, value in obj.items()}
    if isinstance(obj, bytes):
        return {GUMMIES_TYPE: "bytes", "data": str(obj, encoding="utf-8")}
    if isinstance(obj, Exception):
        return {
            GUMMIES_TYPE: "exception",
            "classname": obj.__class__.__name__,
            "module": obj.__class__.__module__,
            "data": serialize_exception(obj),
        }
    return {
        GUMMIES_TYPE: "mock",
        "classname": obj.__class__.__name__,
        "module": obj.__class__.__module__,
    }


def from_serializable_interactions(obj: Any) -> Any:
    """
    Convert a serializable object back to its original form.

    Args:
        obj: The object to be converted.

    Returns:
        The converted object.
    """
    if isinstance(obj, list):
        return [from_serializable_interactions(item) for item in obj]
    if isinstance(obj, set):
        return {from_serializable_interactions(item) for item in obj}
    if isinstance(obj, tuple):
        return tuple(from_serializable_interactions(item) for item in obj)
    if isinstance(obj, dict):
        if obj.get(GUMMIES_TYPE) == "bytes":
            return bytes(obj.get("data"), encoding="utf-8")
        if obj.get(GUMMIES_TYPE) == "exception":
            return deserialize_exception(obj.get("data"))
        if obj.get(GUMMIES_TYPE) == "mock":
            return Mock()
        return {
            key: from_serializable_interactions(value) for key, value in obj.items()
        }
    return obj


def get_json_or_file_path(s: str) -> Union[Dict[str, Any], str, None]:
    """
    Check if the input string is a valid JSON or a valid file path.

    Args:
        s: The input string to be checked.

    Returns:
        If the input string is a valid JSON, return the JSON object and the type 'dict'.
        If the input string is a valid file path, return the file path and the type 'str'.
        If the input string is neither a valid JSON nor a valid file path, return None.
    """
    # Check if s is a valid JSON
    try:
        read_json = json.loads(s)
        if isinstance(read_json, (list, dict)):
            return read_json, type(read_json)
    except json.JSONDecodeError:
        pass

    # Check if s is a valid file path``
    if os.path.isfile(s):
        return s, str

    raise Exception("Unsupported source type or file not found.")

