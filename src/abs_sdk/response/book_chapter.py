"""Created by abs_sdk.devtools.create_module."""

import datetime as dt
from functools import cached_property

from abs_sdk.core import APIResponseModel
from abs_sdk.logging_config import get_logger

logger = get_logger(__name__)


class BookChapterResponse(APIResponseModel):
    id: int
    start: float
    end: float
    title: str

    @cached_property
    def start_timedelta(self) -> dt.timedelta:
        """Convert the start time in seconds to a timedelta object."""
        return dt.timedelta(seconds=self.start)

    @cached_property
    def end_timedelta(self) -> dt.timedelta:
        """Convert the end time in seconds to a timedelta object."""
        return dt.timedelta(seconds=self.end)

    @cached_property
    def duration(self) -> dt.timedelta:
        """Calculate the duration of the chapter as a timedelta object."""
        return self.end_timedelta - self.start_timedelta
