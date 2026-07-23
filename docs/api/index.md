---
icon: lucide/braces
---

# API overview

The SDK exposes a small public API surface centered on
`abs_sdk.AudiobookshelfClient`.

Use the client to connect to an Audiobookshelf server, then call namespace
objects for the areas that are currently implemented:

- `client.me` for current-user endpoints
- `client.libraries` for library endpoints

## Quick start

```python
from abs_sdk import AudiobookshelfClient

with AudiobookshelfClient(
    base_url="https://audiobookshelf.example.com",
    token="your-api-token",
) as client:
    libraries = client.libraries.get_all_libraries()
    me = client.me.get_library_items_in_progress(limit=10)
```

## Client

`AudiobookshelfClient` handles the HTTP session and authentication header for
you. It accepts these keyword-only arguments:

- `base_url`: base URL for the Audiobookshelf server
- `token`: API token used for Bearer authentication
- `timeout_seconds`: request timeout, defaulting to `30.0`
- `verify_ssl`: whether to verify TLS certificates, defaulting to `True`

The client can also be used as a context manager so the underlying HTTP client
is closed automatically.

## Available namespaces

### `me`

Methods on `client.me` return information about the current user:

- `get_library_items_in_progress(limit=None)`
- `get_media_progress(library_item_id, episode_id=None)`

### `libraries`

Methods on `client.libraries` cover the library endpoints that are currently
implemented:

- `get_all_libraries()`
- `get_a_library(library_id)`
- `get_library_items(library_id, ...)`

The `get_library_items` method supports common query parameters such as
`limit`, `page`, `sort`, `filter`, `include`, and flags for `desc`,
`minified`, and `collapseseries`.

## Notes

The API layer is intentionally small right now. When you add new endpoint
groups, place them under `src/abs_sdk/api/` and add a matching section here so
the docs stay aligned with the public client surface.
