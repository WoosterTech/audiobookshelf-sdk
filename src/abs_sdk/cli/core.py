"""CLI-specific core functionality for the SDK."""

from dataclasses import dataclass

from typer import Context

from ..logging_config import set_log_level

__all__ = ["GlobalCLIOptions", "ProjectContext"]


@dataclass
class GlobalCLIOptions:
    """Global options passed to all CLI commands."""

    verbosity: int
    dry_run: bool = False

    def __post_init__(self) -> None:
        set_log_level(self.verbosity)


class ProjectContext(Context):
    """Custom Typer Context that adds the proper typing for `obj`."""

    obj: GlobalCLIOptions
