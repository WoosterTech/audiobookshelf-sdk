"""Created by abs_sdk.devtools.create_module."""

from uuid import UUID  # noqa: TC003

from abs_sdk.core import APIResponseModel
from abs_sdk.logging_config import get_logger

logger = get_logger(__name__)


class DeviceInfoResponse(APIResponseModel):
    """A response model representing device information."""

    id: UUID
    user_id: UUID
    device_id: str
    ip_address: str | None
    browser_name: str | None
    browser_version: str | None
    os_name: str | None
    os_version: str | None
    device_name: str | None
    device_type: str | None
    manufacturer: str | None
    model: str | None
    sdk_version: int | None
    client_name: str
    client_version: str
