"""Created by abs_sdk.devtools.create_module."""

import datetime as dt
from functools import cached_property

from attrmagic.sentinels import MISSING, Missing

from abs_sdk.core import APIResponseModel
from abs_sdk.logging_config import get_logger
from abs_sdk.response.audio_file import AudioFileResponse  # noqa: TC001
from abs_sdk.response.audio_track import AudioTrackResponse  # noqa: TC001
from abs_sdk.response.book_chapter import BookChapterResponse  # noqa: TC001
from abs_sdk.response.book_metadata import (  # noqa: TC001
    BookMetadataResponse,
    BookMetadataResponseExpanded,
    BookMetadataResponseGeneric,
    BookMetadataResponseMinified,
)
from abs_sdk.response.ebook_file import EBookFileResponse  # noqa: TC001

logger = get_logger(__name__)


class _BookResponseBase(APIResponseModel):
    cover_path: str | None
    tags: list[str]


class BookResponse(_BookResponseBase):
    metadata: BookMetadataResponse
    library_item_id: str
    audio_files: list[AudioFileResponse]
    chapters: list[BookChapterResponse]
    ebook_file: EBookFileResponse | None


class BookResponseMinified(_BookResponseBase):
    """A minified version of the BookResponse model, containing only essential fields."""

    metadata: BookMetadataResponseMinified
    num_tracks: int
    num_audio_files: int
    num_chapters: int
    duration: float
    size: int
    ebook_format: str | None = None

    @cached_property
    def duration_timedelta(self) -> "dt.timedelta":
        """Convert the duration in seconds to a timedelta object."""

        return dt.timedelta(seconds=self.duration)


class BookResponseExpanded(_BookResponseBase):
    """An expanded version of the BookResponse model, potentially including additional fields or relationships."""

    metadata: BookMetadataResponseExpanded
    duration: float
    size: int
    tracks: list[AudioTrackResponse]

    @cached_property
    def duration_timedelta(self) -> "dt.timedelta":
        """Convert the duration in seconds to a timedelta object."""

        return dt.timedelta(seconds=self.duration)


class BookResponseGeneric(_BookResponseBase):
    """A generic version of the BookResponse model, which can be used for various purposes where a specific response type is not required."""

    metadata: BookMetadataResponseGeneric
    library_item_id: str | Missing = MISSING
    audio_files: list[AudioFileResponse] | Missing = MISSING
    chapters: list[BookChapterResponse] | Missing = MISSING
    ebook_file: EBookFileResponse | None | Missing = MISSING
    num_tracks: int | Missing = MISSING
    num_audio_files: int | Missing = MISSING
    num_chapters: int | Missing = MISSING
    duration: float | Missing = MISSING
    size: int | Missing = MISSING
    ebook_format: str | None | Missing = MISSING
    tracks: list[AudioTrackResponse] | Missing = MISSING

    @cached_property
    def duration_timedelta(self) -> "dt.timedelta | Missing":
        """Convert the duration in seconds to a timedelta object."""
        if self.duration is MISSING:
            return MISSING
        return dt.timedelta(seconds=self.duration)
