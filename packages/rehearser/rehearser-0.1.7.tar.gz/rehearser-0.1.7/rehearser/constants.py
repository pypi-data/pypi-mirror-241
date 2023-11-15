from enum import Enum


class InteractionType(Enum):
    """
    Enum representing the types of interactions that can be recorded.
    """
    INITIAL = "initial"
    METHOD_CALL = "method_call"
    ATTRIBUTE_ACCESS = "attribute_access"
    ATTRIBUTE_ASSIGNMENT = "attribute_assignment"