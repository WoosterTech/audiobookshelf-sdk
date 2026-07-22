"""Created by abs_sdk.devtools.create_module."""

import datetime as dt
from enum import IntEnum
from functools import cached_property
from uuid import UUID  # noqa: TC003

from attrmagic.sentinels import MISSING, Missing

from abs_sdk.core import APIResponseModel, DayOfWeek, datetime_from_epoch_ms
from abs_sdk.logging_config import get_logger
from abs_sdk.response.audio_track import AudioTrackResponse  # noqa: TC001
from abs_sdk.response.book_chapter import BookChapterResponse  # noqa: TC001
from abs_sdk.response.book_metadata import BookMetadataResponse  # noqa: TC001
from abs_sdk.response.device_info import DeviceInfoResponse  # noqa: TC001
from abs_sdk.response.library_item import LibraryItemResponseExpanded, MediaType  # noqa: TC001

logger = get_logger(__name__)


class PlayMethod(IntEnum):
    DIRECT_PLAY = 0
    DIRECT_STREAM = 1
    TRANSCODE = 2
    LOCAL = 3


class PlaybackSessionResponse(APIResponseModel):
    """A response model representing a playback session."""

    id: UUID
    user_id: UUID
    library_id: UUID
    library_item_id: UUID
    episode_id: UUID | None
    media_type: MediaType
    # TODO: Add "PodcastMetdataResponse" when Podcast support is added
    media_metadata: BookMetadataResponse
    chapters: list[BookChapterResponse]
    display_title: str
    display_author: str
    cover_path: str
    duration: float
    play_method: PlayMethod
    media_player: str
    device_info: DeviceInfoResponse
    server_version: str
    date: str
    day_of_week: DayOfWeek
    time_listening: float
    start_time: float
    current_time: float
    started_at: int
    updated_at: int

    @cached_property
    def duration_timedelta(self) -> "dt.timedelta":
        """Convert the duration in seconds to a timedelta object."""
        return dt.timedelta(seconds=self.duration)

    @property
    def date_date(self) -> "dt.date":
        """Convert the date string to a date object."""
        return dt.datetime.strptime(self.date, "%Y-%m-%d").date()

    @cached_property
    def time_listening_timedelta(self) -> "dt.timedelta":
        """Convert the time_listening in seconds to a timedelta object."""
        return dt.timedelta(seconds=self.time_listening)

    @cached_property
    def start_time_timedelta(self) -> "dt.timedelta":
        """Convert the start_time in seconds to a timedelta object."""
        return dt.timedelta(seconds=self.start_time)

    @cached_property
    def current_time_timedelta(self) -> "dt.timedelta":
        """Convert the current_time in seconds to a timedelta object."""
        return dt.timedelta(seconds=self.current_time)

    @cached_property
    def started_at_datetime(self) -> "dt.datetime":
        """Convert the started_at timestamp to a datetime object."""
        return datetime_from_epoch_ms(self.started_at)

    @cached_property
    def updated_at_datetime(self) -> "dt.datetime":
        """Convert the updated_at timestamp to a datetime object."""
        return datetime_from_epoch_ms(self.updated_at)


class PlaybackSessionResponseExpanded(PlaybackSessionResponse):
    """An expanded version of the PlaybackSessionResponse model, potentially including additional fields or relationships."""

    audio_tracks: list[AudioTrackResponse]
    # TODO: Add `video_tracks` when Video support is added
    video_track: object | None
    library_item: LibraryItemResponseExpanded


class PlaybackSessionResponseGeneric(PlaybackSessionResponse):
    """A generic version of the PlaybackSessionResponse model, which can be used for various purposes where a specific response type is not required."""

    audio_tracks: list[AudioTrackResponse] | Missing = MISSING
    video_track: object | None | Missing = MISSING
    library_item: LibraryItemResponseExpanded | Missing = MISSING
