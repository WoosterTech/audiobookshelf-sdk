"""Created by abs_sdk.devtools.create_module."""

import datetime as dt
from functools import cached_property

from abs_sdk.core import APIResponseModel, datetime_from_epoch_ms
from abs_sdk.logging_config import get_logger

logger = get_logger(__name__)


class AudioBookmarkResponse(APIResponseModel):
    """A response model representing an audio bookmark."""

    library_item_id: str
    title: str
    time: int
    created_at: int

    @cached_property
    def time_timedelta(self) -> "dt.timedelta":
        """Convert the time in seconds to a timedelta object."""
        return dt.timedelta(seconds=self.time)

    @cached_property
    def created_at_datetime(self) -> "dt.datetime":
        """Convert the created_at timestamp to a datetime object."""
        return datetime_from_epoch_ms(self.created_at)
