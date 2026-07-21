"""Created by abs_sdk.devtools.create_module."""

from functools import cached_property
from typing import TYPE_CHECKING

from abs_sdk.core import APIResponseModel, datetime_from_epoch_ms
from abs_sdk.logging_config import get_logger

if TYPE_CHECKING:
    import datetime as dt
logger = get_logger(__name__)


class FileMetadataResponse(APIResponseModel):
    filename: str
    ext: str
    path: str
    rel_path: str
    size: int
    mtime_ms: int
    ctime_ms: int
    birthtime_ms: int

    @cached_property
    def mtime_datetime(self) -> "dt.datetime":
        """Convert the mtime timestamp to a datetime object."""
        return datetime_from_epoch_ms(self.mtime_ms)

    @cached_property
    def ctime_datetime(self) -> "dt.datetime":
        """Convert the ctime timestamp to a datetime object."""
        return datetime_from_epoch_ms(self.ctime_ms)

    @cached_property
    def birthtime_datetime(self) -> "dt.datetime":
        """Convert the birthtime timestamp to a datetime object."""
        return datetime_from_epoch_ms(self.birthtime_ms)
