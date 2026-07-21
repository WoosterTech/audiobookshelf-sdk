"""Created by abs_sdk.devtools.create_module."""

from functools import cached_property
from typing import TYPE_CHECKING

from abs_sdk.core import APIResponseModel, datetime_from_epoch_ms
from abs_sdk.logging_config import get_logger
from abs_sdk.response.file_metadata import FileMetadataResponse  # noqa: TC001

if TYPE_CHECKING:
    import datetime as dt

logger = get_logger(__name__)


class LibraryFileResponse(APIResponseModel):
    """A response model representing a library file."""

    ino: str
    metadata: FileMetadataResponse
    added_at: int
    updated_at: int
    file_type: str

    @cached_property
    def added_at_datetime(self) -> "dt.datetime":
        """Convert the added_at timestamp to a datetime object."""
        return datetime_from_epoch_ms(self.added_at)

    @cached_property
    def updated_at_datetime(self) -> "dt.datetime":
        """Convert the updated_at timestamp to a datetime object."""
        return datetime_from_epoch_ms(self.updated_at)
