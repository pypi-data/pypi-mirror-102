from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar

from templ8.services.exceptions import MissingOutputDir
from templ8.utils.dicts import collapse_dict, key_is_true
from templ8.utils.files import parse_file
from templ8.utils.paths import abs_from_root, path_head
from templ8.utils.types import filter_dataclass_input

T = TypeVar("T", bound="Inputs")  #  pylint: disable = C0103


@dataclass
class Inputs:
    output_dir: str
    clear_top_level: bool = False
    logical_grouping: bool = False
    includes: List[str] = field(default_factory=list)
    protected: List[str] = field(default_factory=list)
    collections: List[str] = field(default_factory=list)
    render_context: Dict[str, Any] = field(default_factory=dict)
    collection_sources: List[str] = field(default_factory=list)
    loader_paths: List[str] = field(default_factory=list)

    @classmethod
    def from_file(cls: Type[T], input_file: str) -> T:
        input_config = filter_dataclass_input(
            cls, parse_file(input_file)
        )

        if "output_dir" not in input_config:
            raise MissingOutputDir()

        if (
            key_is_true(input_config, "logical_grouping")
            and "render_context" in input_config
        ):
            input_config["render_context"] = collapse_dict(
                input_config["render_context"]
            )

        if "loader_paths" in input_config:
            input_config["loader_paths"] = [
                abs_from_root(input_file, i)
                for i in input_config["loader_paths"]
            ]

        protected_inputs = [path_head(input_file)]

        if "protected" in input_config:
            input_config["protected"] += protected_inputs

        else:
            input_config["protected"] = protected_inputs

        return cls(**input_config)
