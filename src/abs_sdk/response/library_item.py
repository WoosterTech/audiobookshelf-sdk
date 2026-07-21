"""Created by abs_sdk.devtools.create_module."""

from enum import StrEnum
from functools import cached_property
from typing import TYPE_CHECKING

from attrmagic.sentinels import MISSING, Missing

from abs_sdk.core import APIResponseModel, datetime_from_epoch_ms
from abs_sdk.logging_config import get_logger
from abs_sdk.response.book import (  # noqa: TC001
    BookResponse,
    BookResponseExpanded,
    BookResponseGeneric,
    BookResponseMinified,
)
from abs_sdk.response.library_file import LibraryFileResponse  # noqa: TC001
from abs_sdk.response.podcast import PodcastResponse  # noqa: TC001

if TYPE_CHECKING:
    import datetime as dt

logger = get_logger(__name__)


class MediaType(StrEnum):
    BOOK = "book"
    PODCAST = "podcast"


class _LibraryItemResponseBase(APIResponseModel):
    """Base class for library item responses, containing common fields."""

    id: str
    ino: str
    library_id: str
    folder_id: str
    path: str
    rel_path: str
    is_file: bool
    mtime_ms: int
    ctime_ms: int
    birthtime_ms: int
    added_at: int
    updated_at: int
    is_missing: bool
    is_invalid: bool
    media_type: MediaType

    @cached_property
    def added_at_datetime(self) -> "dt.datetime":
        return datetime_from_epoch_ms(self.added_at)

    @cached_property
    def updated_at_datetime(self) -> "dt.datetime":
        return datetime_from_epoch_ms(self.updated_at)

    @cached_property
    def mtime_datetime(self) -> "dt.datetime":
        return datetime_from_epoch_ms(self.mtime_ms)

    @cached_property
    def ctime_datetime(self) -> "dt.datetime":
        return datetime_from_epoch_ms(self.ctime_ms)

    @cached_property
    def birthtime_datetime(self) -> "dt.datetime":
        return datetime_from_epoch_ms(self.birthtime_ms)


class LibraryItemResponse(_LibraryItemResponseBase):
    """A response model representing a library item."""

    last_scan: int | None
    scan_version: str | None
    library_files: list[LibraryFileResponse]
    media: BookResponse | PodcastResponse


class LibraryItemResponseMinified(_LibraryItemResponseBase):
    """A minified version of the LibraryItemResponse model, containing only essential fields."""

    # TODO: implement PodcastResponseMinified if needed, currently only BookResponseMinified is used
    media: BookResponseMinified

    num_files: int
    size: int


class LibraryItemResponseExpanded(_LibraryItemResponseBase):
    """An expanded version of the LibraryItemResponse model, potentially including additional fields or relationships."""

    last_scan: int | None
    scan_version: str | None
    library_files: list[LibraryFileResponse]
    # TODO: implement PodcastResponseExpanded if needed, currently only BookResponseExpanded is used
    media: BookResponseExpanded

    size: int


class LibraryItemResponseGeneric(_LibraryItemResponseBase):
    """A generic version of the LibraryItemResponse model, which can be used for various purposes where a specific response type is not required."""

    last_scan: int | None | Missing = MISSING
    scan_version: str | None | Missing = MISSING
    library_files: list[LibraryFileResponse] | Missing = MISSING
    media: BookResponseGeneric | PodcastResponse | Missing = MISSING

    num_files: int | Missing = MISSING
    size: int | Missing = MISSING
