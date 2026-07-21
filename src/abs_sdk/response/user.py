"""Created by abs_sdk.devtools.create_module."""

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from abs_sdk.core import APIResponseModel, SecretToken
from abs_sdk.logging_config import get_logger
from abs_sdk.response.audio_bookmark import AudioBookmarkResponse  # noqa: TC001
from abs_sdk.response.media_progress import (  # noqa: TC001
    MediaProgressResponse,
    MediaProgressResponseWithMedia,
)
from abs_sdk.response.playback_session import PlaybackSessionResponseExpanded  # noqa: TC001
from abs_sdk.response.user_permissions import UserPermissionsResponse  # noqa: TC001

logger = get_logger(__name__)


class UserType(StrEnum):
    USER = "user"
    ADMIN = "admin"
    GUEST = "guest"
    ROOT = "root"


class _UserResponseBase(APIResponseModel):
    id: str
    username: str
    _type: Annotated[UserType, Field(alias="type")]
    last_seen: int | None = None
    created_at: int


class _UserResponseCommon(_UserResponseBase):
    """A response model representing a user."""

    token: SecretToken
    series_hide_from_continue_listening: list[str]
    bookmarks: list[AudioBookmarkResponse]
    is_active: bool
    is_locked: bool
    permissions: UserPermissionsResponse
    libraries_accessible: list[str]
    item_tags_accessible: list[str]


class UserResponse(_UserResponseCommon):
    """A response model representing a user with media progress information."""

    media_progress: list[MediaProgressResponse]


class UserResponseWithProgressDetails(_UserResponseCommon):
    """A response model representing a user with media progress information."""

    media_progress: list[MediaProgressResponseWithMedia]


class UserResponseWithSession(_UserResponseBase):
    """A response model representing a user with session information."""

    session: PlaybackSessionResponseExpanded | None
