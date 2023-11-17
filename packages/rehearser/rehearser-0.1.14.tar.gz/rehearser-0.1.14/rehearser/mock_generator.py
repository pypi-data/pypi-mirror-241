import copy
import json
from typing import Any, Callable, Dict, List, Union
from unittest.mock import MagicMock, Mock, PropertyMock

from rehearser.constants import (GUMMIES_INTERACTIONS_FILE_TYPE,
                                 INTERACTIONS_KEY, InteractionType,
                                 SupportedInteractionsType)
from rehearser.utils import (from_serializable_interactions,
                             get_json_or_file_path)


class MockGenerator:
    def __init__(
        self, interactions_src: Union[str, Dict[str, Any], List[Dict[str, Any]]]
    ):
        """
        Initialize the MockGenerator with interactions source.
        Args:
            interactions_src: The source of interactions, either a JSON string or a dictionary.
        """
        self._method_interactions = {}
        self._attribute_interactions = {}
        self._interactions_src_type = None
        self.load_interactions_src(interactions_src)


    def load_interactions_src(self, interactions_src: Union[str, Dict[str, Any]]) -> Any:
        """"
        Load interactions source.
        
        Args:
            interactions_src: filename or a JSON string or a dictionary.
        """
        if isinstance(interactions_src, str):
            interactions_src, py_type = get_json_or_file_path(interactions_src)
            if py_type == str:
                with open(interactions_src) as f:
                    interactions_src = json.load(f)
        # make sure interactions_src is a dictionary or list now

        if isinstance(interactions_src, dict):
            # extract interactions_src_type and the list form of interactions
            self._interactions_src_type = interactions_src.get(
                GUMMIES_INTERACTIONS_FILE_TYPE,
                SupportedInteractionsType.PYTHON_INSTANCE.name,
            )
            if self._interactions_src_type in (
                SupportedInteractionsType.PYTHON_INSTANCE.name,
                SupportedInteractionsType.PYTHON_CALLABLE.name,
            ):
                interactions_src = interactions_src[INTERACTIONS_KEY]
            else:
                raise NotImplementedError(
                    f"Unsupported interactions type: {interactions_src[GUMMIES_INTERACTIONS_FILE_TYPE]}"
                )
        elif isinstance(interactions_src, list):
            self._interactions_src_type = SupportedInteractionsType.PYTHON_INSTANCE.name
            pass
        if not self._interactions_src_type:
            raise NotImplementedError(
                f"Unsupported interactions type: {type(interactions_src)}"
            )

        # interactions_src is supposed to be a list now
        interactions = from_serializable_interactions(interactions_src)
        for interaction in interactions:
            if interaction["type"] in (
                InteractionType.INSTANCE_METHOD_CALL.name,
                InteractionType.METHOD_CALL.name,
            ):
                if interaction["name"] not in self._method_interactions:
                    self._method_interactions[interaction["name"]] = []
                self._method_interactions[interaction["name"]].append(interaction)
            elif interaction["type"] == InteractionType.ATTRIBUTE_ACCESS.name:
                if interaction["name"] not in self._attribute_interactions:
                    self._attribute_interactions[interaction["name"]] = []
                self._attribute_interactions[interaction["name"]].append(interaction)
        
        return self
        

    def create_mock(self) -> Union[MagicMock, Mock, Callable]:
        """
        Create a mock object based on the interactions.

        Returns:
            A mock object with methods and attributes set based on the interactions.
        """
        mock = MagicMock()

        if (
            self._interactions_src_type
            == SupportedInteractionsType.PYTHON_INSTANCE.name
        ):
            # all methods share the same interactions log
            attr_side_effect = {}
            for attr_name, interactions in self._attribute_interactions.items():
                attr_side_effect[attr_name] = []
                for attr_info in interactions:
                    attr_side_effect[attr_name].append(attr_info.get("result"))
            for attr_name in self._attribute_interactions.keys():
                setattr(
                    type(mock),
                    attr_name,
                    PropertyMock(side_effect=attr_side_effect[attr_name]),
                )

            # all methods share the same interactions log
            for method_name, interactions in self._method_interactions.items():
                setattr(
                    mock,
                    method_name,
                    Mock(side_effect=self._get_side_effect(interactions)),
                )
            return mock
        elif (
            self._interactions_src_type
            == SupportedInteractionsType.PYTHON_CALLABLE.name
        ):
            return self._get_side_effect(list(self._method_interactions.values())[0])

    def _get_side_effect(self, interactions: List[Dict[str, Any]]) -> Callable:
        """
        Get the side effect function for a mock method.

        Args:
            interactions: The list of interactions for the method.

        Returns:
            A function that can be used as the side effect for the mock method.
        """
        # make sure every mock created has its own copy of interactions
        _get_side_effect_interactions = copy.deepcopy(interactions)

        def side_effect(*args: Any, **kwargs: Any) -> Any:
            """
            The side effect function for the mock method.

            Args:
                *args: The positional arguments for the method call.
                **kwargs: The keyword arguments for the method call.

            Returns:
                The result of the method call, if it was recorded in the interactions.
            """
            if not _get_side_effect_interactions:
                raise StopIteration
            interaction = _get_side_effect_interactions.pop(0)
            if "result" in interaction:
                return interaction["result"]
            elif "exception" in interaction:
                raise interaction["exception"]

        return side_effect
