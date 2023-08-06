import json
import os
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Type, TypeVar

from walkmate import get_child_files

from templ8.models.initialization import Initialization
from templ8.models.template import Template
from templ8.services.exceptions import (
    CollectionsSourcePathError,
    InvalidMetadata,
)
from templ8.services.jinja import combine_schemas
from templ8.utils.lists import filter_includes
from templ8.utils.paths import (
    get_module_path,
    is_path_head,
    path_ext,
    path_head,
)
from templ8.utils.types import filter_dataclass_input

T = TypeVar("T", bound="Collection")  #  pylint: disable = C0103

core_templates_source = os.path.normpath(
    os.path.join(__file__, "..", "..", "core")
)


@dataclass
class Collection:
    path: str

    # Source properties
    templates: List[Template]
    static_files: List[str]

    # Metadata fields
    default_variables: Dict[str, Any] = field(default_factory=dict)
    dynamic_folders: Dict[str, str] = field(default_factory=dict)
    default_protected: List[str] = field(default_factory=list)
    initialization: List[Initialization] = field(default_factory=list)

    def __repr__(self) -> str:
        count = len(self.templates) + len(self.static_files)
        unit = "files" if count != 1 else "file"
        return f"({path_head(self.path)}: {count} {unit})"

    @classmethod
    def from_metadata(
        cls: Type[T], path: str, includes: List[str]
    ) -> T:
        with open(os.path.join(path, "metadata.json"), "r") as stream:
            try:
                metadata = filter_dataclass_input(
                    cls, json.load(stream)
                )

            except json.decoder.JSONDecodeError as err:
                raise InvalidMetadata(path) from err

        all_files = [
            os.path.relpath(file, path)
            for file in get_child_files(path)
        ]

        templates = filter_includes(
            [
                Template(path, file)
                for file in all_files
                if path_ext(file) == ".j2"
            ],
            includes,
            lambda x: x.output_path,
        )

        static_files = filter_includes(
            [
                file
                for file in all_files
                if path_ext(file) != ".j2" and file != "metadata.json"
            ],
            includes,
        )

        if "initialization" in metadata:
            initialization = [
                Initialization.parse(i)
                for i in metadata.pop("initialization")
            ]

        else:
            initialization = []

        return cls(
            path,
            **metadata,
            templates=templates,
            static_files=static_files,
            initialization=initialization,
        )

    @classmethod
    def gather(
        cls: Type[T],
        collections: Optional[List[str]] = None,
        includes: Optional[List[str]] = None,
        collection_sources: Optional[List[str]] = None,
    ) -> List[T]:
        if not collection_sources:
            collection_sources = []

        collection_sources = [
            get_module_path(path) if is_path_head(path) else path
            for path in collection_sources
        ]

        collection_sources.append(core_templates_source)

        for path in collection_sources:
            if not os.path.exists(path):
                raise CollectionsSourcePathError(path)

        discovered = [
            os.path.join(collection_source, subdir)
            for collection_source in collection_sources
            for subdir in os.listdir(collection_source)
        ]

        specified = [
            cls.from_metadata(source, (includes or []))
            for source in discovered
            if os.path.isdir(source)
            and "metadata.json" in os.listdir(source)
            and path_head(source) in (collections or [])
        ]

        return sorted(
            specified,
            key=lambda x: (collections or []).index(
                path_head(x.path)
            ),
        )

    @property
    def schema(self) -> Dict[str, Any]:
        return combine_schemas(self.templates)
