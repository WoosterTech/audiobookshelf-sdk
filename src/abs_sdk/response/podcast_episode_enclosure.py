"""Created by abs_sdk.devtools.create_module."""

from typing import Annotated

from pydantic import Field

from abs_sdk.core import APIResponseModel
from abs_sdk.logging_config import get_logger

logger = get_logger(__name__)


class PodcastEpisodeEnclosureResponse(APIResponseModel):
    """A response model representing a podcast episode enclosure."""

    url: str
    length: int
    _type: Annotated[str, Field(alias="type")]
