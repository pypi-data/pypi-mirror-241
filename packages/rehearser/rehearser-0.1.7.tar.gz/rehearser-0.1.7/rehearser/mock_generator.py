import json
from typing import Any, Callable, Dict, List, Union
from unittest.mock import MagicMock, Mock, PropertyMock

from rehearser.constants import InteractionType
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
        if isinstance(interactions_src, str):
            interactions_src, src_type = get_json_or_file_path(interactions_src)
            if not src_type:
                return
            if src_type == str:
                with open(interactions_src) as f:
                    interactions_src = json.load(f)

        interactions = from_serializable_interactions(interactions_src)
        for interaction in interactions:
            if interaction["type"] == InteractionType.METHOD_CALL.name:
                if interaction["name"] not in self._method_interactions:
                    self._method_interactions[interaction["name"]] = []
                self._method_interactions[interaction["name"]].append(interaction)
            elif interaction["type"] == InteractionType.ATTRIBUTE_ACCESS.name:
                if interaction["name"] not in self._attribute_interactions:
                    self._attribute_interactions[interaction["name"]] = []
                self._attribute_interactions[interaction["name"]].append(interaction)

    def create_mock(self):
        """
        Create a mock object based on the interactions.

        Returns:
            A mock object with methods and attributes set based on the interactions.
        """
        mock = MagicMock()

        # all methods share the same interactions log
        attr_side_effect = {}
        for attr_name, interactions in self._attribute_interactions.items():
            attr_side_effect[attr_name] = []
            for attr_info in interactions:
                attr_side_effect[attr_name].append(attr_info.get("result"))
        for attr_name in self._attribute_interactions.keys():
            print(
                f"attr_name: {attr_name}, attr_side_effect: {attr_side_effect[attr_name]}"
            )
            setattr(
                type(mock),
                attr_name,
                PropertyMock(side_effect=attr_side_effect[attr_name]),
            )

        # all methods share the same interactions log
        for method_name, interactions in self._method_interactions.items():
            setattr(
                mock, method_name, Mock(side_effect=self._get_side_effect(interactions))
            )
        return mock

    def _get_side_effect(self, interactions: List[Dict[str, Any]]) -> Callable:
        """
        Get the side effect function for a mock method.

        Args:
            interactions: The list of interactions for the method.

        Returns:
            A function that can be used as the side effect for the mock method.
        """

        def side_effect(*args: Any, **kwargs: Any) -> Any:
            """
            The side effect function for the mock method.

            Args:
                *args: The positional arguments for the method call.
                **kwargs: The keyword arguments for the method call.

            Returns:
                The result of the method call, if it was recorded in the interactions.
            """
            if not interactions:
                raise StopIteration
            interaction = interactions.pop(0)
            if "result" in interaction:
                return interaction["result"]
            elif "exception" in interaction:
                raise interaction["exception"]

        return side_effect
