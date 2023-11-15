from enum import Enum

GUMMIES_TYPE = "__gummies#type__"
GUMMIES_INTERACTIONS_FILE_TYPE = "__gummies#interactios#file#type__"
INTERACTIONS_KEY = "interactions"
INTERACTIONS_RAW_FILE_DEFAULT_DIRECTORY = "./raw_files/rehearser_proxy/"

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
    PYTHON_INSTANCE = (
        "python_instance"  # default as PYTHON_INSTANCE if interaction type is an array
    )
    PYTHON_CALLABLE = "python_callable"
