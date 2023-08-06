from dataclasses import dataclass
from typing import Dict, Type, TypeVar, Union

from templ8.services.exceptions import InvalidInitialization

T = TypeVar("T", bound="Initialization")  #  pylint: disable = C0103


@dataclass
class Initialization:
    cmd: str
    cwd: str

    @classmethod
    def parse(cls: Type[T], obj: Union[str, Dict[str, str]]) -> T:
        if isinstance(obj, str):
            return cls(cmd=obj, cwd=".")

        if not isinstance(obj, dict) or "cmd" not in obj:
            raise InvalidInitialization()

        return cls(obj["cmd"], obj["cwd"] if "cwd" in obj else ".")
