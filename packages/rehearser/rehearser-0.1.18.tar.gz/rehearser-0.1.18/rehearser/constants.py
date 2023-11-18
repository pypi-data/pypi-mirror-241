from enum import Enum

GUMMIES_TYPE = "__gummies#type__"
GUMMIES_INTERACTIONS_FILE_TYPE = "__gummies#interactios#file#type__"
INTERACTIONS_KEY = "interactions"
INTERACTIONS_RAW_FILE_DEFAULT_DIRECTORY = "./raw_files/rehearser_proxy/"
REHEARSER_PROXY_FILTERED_ATTRS = [
    "__rehearser_type",
    "__obj",
    "__interaction",
    "__mock",
    "interactions_file_directory",
    "interactions_file_name",
    "interactions_file_dir_path_name",
    "scenario_name",
    "entity_id",
    "use_timestamp",
    "bucket_name"
]


class RehearserType(Enum):
    """
    Enum representing the types of rehearsers that can be used.
    """

    METHOD = "method"
    INSTANCE = "instance"


class InteractionType(Enum):
    """
    Enum representing the types of interactions that can be recorded.
    """

    INITIAL = "initial"
    METHOD_CALL = "method_call"
    INSTANCE_METHOD_CALL = "instance_method_call"
    ATTRIBUTE_ACCESS = "attribute_access"
    ATTRIBUTE_ASSIGNMENT = "attribute_assignment"


class SupportedInteractionsType(Enum):
    """
    Enum representing the types of interactions that can be recorded.
    """
    PYTHON_INSTANCE = "python_instance"  # default as PYTHON_INSTANCE if interaction type is an array
    PYTHON_CALLABLE = "python_callable"
