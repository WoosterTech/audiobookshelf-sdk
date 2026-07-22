"""Created by abs_sdk.devtools.create_module."""

import datetime as dt
from functools import cached_property

from abs_sdk.core import APIResponseModel
from abs_sdk.logging_config import get_logger
from abs_sdk.response.file_metadata import FileMetadataResponse  # noqa: TC001

logger = get_logger(__name__)


class AudioTrackResponse(APIResponseModel):
    index: int
    start_offset: float
    duration: float
    title: str
    content_url: str
    mime_type: str
    metadata: FileMetadataResponse | None

    @cached_property
    def start_offset_timedelta(self) -> "dt.timedelta":
        """Convert the start_offset in seconds to a timedelta object."""
        return dt.timedelta(seconds=self.start_offset)

    @cached_property
    def duration_timedelta(self) -> "dt.timedelta":
        """Convert the duration in seconds to a timedelta object."""
        return dt.timedelta(seconds=self.duration)
