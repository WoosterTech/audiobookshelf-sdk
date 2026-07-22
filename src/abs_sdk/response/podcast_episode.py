"""Created by abs_sdk.devtools.create_module."""

from datetime import timedelta

from abs_sdk.core import APIResponseModel, datetime_from_epoch_ms
from abs_sdk.logging_config import get_logger
from abs_sdk.response.audio_file import AudioFileResponse  # noqa: TC001
from abs_sdk.response.audio_track import AudioTrackResponse  # noqa: TC001
from abs_sdk.response.podcast_episode_enclosure import (
    PodcastEpisodeEnclosureResponse,  # noqa: TC001
)

logger = get_logger(__name__)


class PodcastEpisodeResponse(APIResponseModel):
    """A response model representing a podcast episode."""

    library_item_id: str
    id: str
    index: int
    season: str
    episode: str
    episode_type: str
    title: str
    subtitle: str
    description: str
    enclosure: PodcastEpisodeEnclosureResponse
    pub_date: str
    audio_file: AudioFileResponse
    published_at: int
    added_at: int
    updated_at: int

    @property
    def pub_date_datetime(self):
        """Return the publication date as a datetime object."""

        return datetime_from_epoch_ms(self.published_at)

    @property
    def added_at_datetime(self):
        """Return the added date as a datetime object."""

        return datetime_from_epoch_ms(self.added_at)

    @property
    def updated_at_datetime(self):
        """Return the updated date as a datetime object."""

        return datetime_from_epoch_ms(self.updated_at)


class PodcastEpisodeResponseExpanded(PodcastEpisodeResponse):
    """A response model representing a podcast episode with expanded information."""

    audio_track: AudioTrackResponse
    duration: float
    size: int

    @property
    def duration_timedelta(self) -> "timedelta":
        """Return the duration as a timedelta object."""

        return timedelta(seconds=self.duration)
