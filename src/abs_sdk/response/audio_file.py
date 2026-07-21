"""Created by abs_sdk.devtools.create_module."""

import datetime as dt
from functools import cached_property

from pydantic import Field

from abs_sdk.core import APIResponseModel, datetime_from_epoch_ms
from abs_sdk.logging_config import get_logger
from abs_sdk.response.book_chapter import BookChapterResponse  # noqa: TC001
from abs_sdk.response.file_metadata import FileMetadataResponse  # noqa: TC001

logger = get_logger(__name__)


class AudioFileResponse(APIResponseModel):
    index: int
    ino: str
    metadata: FileMetadataResponse
    added_at: int
    updated_at: int
    track_num_from_meta: int | None = None
    disc_num_from_meta: int | None = None
    track_num_from_filename: int | None = None
    disc_num_from_filename: int | None = None
    manually_verified: bool
    exclude: bool
    error: str | None = None
    format: str
    duration: float
    bit_rate: int
    language: str | None = None
    codec: str
    time_base: str
    channels: int
    channel_layout: str
    chapters: list[BookChapterResponse]
    embedded_cover_art: str | None = None
    meta_tags: dict[str, object] = Field(default_factory=dict)
    mime_type: str

    @cached_property
    def added_at_datetime(self) -> "dt.datetime":
        """Convert the added_at timestamp to a datetime object."""
        return datetime_from_epoch_ms(self.added_at)

    @cached_property
    def updated_at_datetime(self) -> "dt.datetime":
        """Convert the updated_at timestamp to a datetime object."""
        return datetime_from_epoch_ms(self.updated_at)

    @cached_property
    def duration_timedelta(self) -> "dt.timedelta":
        """Convert the duration in seconds to a timedelta object."""
        return dt.timedelta(seconds=self.duration)
