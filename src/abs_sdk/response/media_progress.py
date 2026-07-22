"""Created by abs_sdk.devtools.create_module."""

import datetime as dt
from functools import cached_property
from typing import TYPE_CHECKING, override

from attrmagic.sentinels import MISSING, Missing

from abs_sdk.core import APIResponseModel, datetime_from_epoch_ms
from abs_sdk.logging_config import get_logger
from abs_sdk.response.book import BookResponseExpanded  # noqa: TC001
from abs_sdk.response.podcast_episode import PodcastEpisodeResponse  # noqa: TC001

if TYPE_CHECKING:
    import rich.repr

logger = get_logger(__name__)


class MediaProgressResponse(APIResponseModel):
    """A response model representing the progress of media playback."""

    id: str
    library_item_id: str
    episode_id: str | None
    duration: float
    progress: float
    current_time: float
    is_finished: bool
    hide_from_continue_listening: bool
    last_update: int
    started_at: int
    finished_at: int | None

    @cached_property
    def duration_timedelta(self) -> "dt.timedelta":
        """Convert the duration in seconds to a timedelta object."""
        return dt.timedelta(seconds=self.duration)

    @cached_property
    def current_time_timedelta(self) -> "dt.timedelta":
        """Convert the current_time in seconds to a timedelta object."""
        return dt.timedelta(seconds=self.current_time)

    @cached_property
    def last_update_datetime(self) -> "dt.datetime":
        """Convert the last_update timestamp to a datetime object."""
        return datetime_from_epoch_ms(self.last_update)

    @cached_property
    def started_at_datetime(self) -> "dt.datetime":
        """Convert the started_at timestamp to a datetime object."""
        return datetime_from_epoch_ms(self.started_at)

    @cached_property
    def finished_at_datetime(self) -> "dt.datetime | None":
        """Convert the finished_at timestamp to a datetime object, if available."""
        return datetime_from_epoch_ms(self.finished_at) if self.finished_at is not None else None

    @override
    def __rich_repr__(self) -> "rich.repr.Result":
        yield "id", self.id
        yield "library_item_id", self.library_item_id
        yield "episode_id", self.episode_id
        yield "duration", self.duration_timedelta
        yield "progress", self.progress
        yield "current_time", self.current_time_timedelta
        yield "is_finished", self.is_finished
        yield "hide_from_continue_listening", self.hide_from_continue_listening
        yield "last_update", self.last_update_datetime
        yield "started_at", self.started_at_datetime
        yield "finished_at", self.finished_at_datetime if self.finished_at is not None else None


class MediaProgressResponseWithMedia(MediaProgressResponse):
    """A response model representing the progress of media playback, including associated media information."""

    media: BookResponseExpanded
    episode: PodcastEpisodeResponse | Missing = MISSING


class MediaProgressResponseGeneric(MediaProgressResponse):
    """A generic version of the MediaProgressResponse model, which can be used for various purposes where a specific response type is not required."""

    media: BookResponseExpanded | Missing = MISSING
    episode: PodcastEpisodeResponse | Missing = MISSING
