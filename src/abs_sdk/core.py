"""Project level core functionality that doesn't fit into a more specific module."""

import datetime
from dataclasses import dataclass
from enum import StrEnum
from os import PathLike
from typing import override

from attrmagic import ClassBase
from pydantic import ConfigDict, SecretStr
from pydantic.alias_generators import to_camel
from typer import Context

from .logging_config import get_logger, set_log_level

logger = get_logger(__name__)

# A type alias for inputs that can be either a string or a PathLike object representing a filesystem path. This is used for type annotations in functions that accept file paths, allowing for flexibility in the types of path inputs while maintaining type safety.
type PathInput = PathLike[str] | str


@dataclass
class GlobalCLIOptions:
    verbosity: int
    dry_run: bool = False

    def __post_init__(self) -> None:
        set_log_level(self.verbosity)


class ProjectContext(Context):
    """Custom Typer Context that adds the proper typing for `obj`."""

    obj: GlobalCLIOptions


class APIModel(ClassBase):
    model_config: ConfigDict = ConfigDict(alias_generator=to_camel)  # pyright: ignore[reportIncompatibleVariableOverride]


class APIResponseModel(APIModel):
    model_config: ConfigDict = ConfigDict(alias_generator=to_camel, frozen=True)


class SecretToken(SecretStr):
    @override
    def _display(self) -> str:
        return "********"


def datetime_from_epoch_ms(epoch_ms: int) -> datetime.datetime:
    """Convert epoch milliseconds to a datetime object."""
    return datetime.datetime.fromtimestamp(epoch_ms / 1000.0)


class DayOfWeek(StrEnum):
    """An enumeration representing the days of the week."""

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
