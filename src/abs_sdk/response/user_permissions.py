"""Created by abs_sdk.devtools.create_module."""

from abs_sdk.core import APIResponseModel
from abs_sdk.logging_config import get_logger

logger = get_logger(__name__)


class UserPermissionsResponse(APIResponseModel):
    """A response model representing user permissions."""

    download: bool
    update: bool
    delete: bool
    upload: bool
    access_all_libraries: bool
    access_all_tags: bool
    access_explicit_content: bool
