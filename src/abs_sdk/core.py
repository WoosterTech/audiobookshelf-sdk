"""Project level core functionality that doesn't fit into a more specific module."""

import datetime
from collections.abc import Mapping, Sequence
from enum import StrEnum
from os import PathLike
from typing import override

import httpx
from attrmagic import ClassBase
from pydantic import ConfigDict, SecretStr
from pydantic.alias_generators import to_camel
from yarl import URL

from .logging_config import get_logger

logger = get_logger(__name__)

# A type alias for inputs that can be either a string or a PathLike object representing a filesystem path. This is used for type annotations in functions that accept file paths, allowing for flexibility in the types of path inputs while maintaining type safety.
type PathInput = PathLike[str] | str

# type aliases from httpx and yarl for better type hinting in the client code
type QueryValue = str | int | float | bool | None
type HeaderTypes = (
    httpx.Headers
    | Mapping[str, str]
    | Mapping[bytes, bytes]
    | Sequence[tuple[str, str]]
    | Sequence[tuple[bytes, bytes]]
)
type PrimitiveData = str | int | float | bool | None
type URLTypes = URL | str
type QueryParamTypes = (
    httpx.QueryParams
    | Mapping[str, PrimitiveData | Sequence[PrimitiveData]]
    | list[tuple[str, PrimitiveData]]
    | tuple[tuple[str, PrimitiveData], ...]
    | str
    | bytes
)


class MediaType(StrEnum):
    BOOK = "book"
    PODCAST = "podcast"


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
