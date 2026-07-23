"""Main CLI entry point for the SDK."""

from typing import Annotated

import typer
from typer import Option as TyperOption

from ..logging_config import get_console
from .core import GlobalCLIOptions, ProjectContext
from .devtools import app as devtools_cli


def verbosity_option(
    help_text: str = "Increase verbosity level (can be used multiple times)",
) -> object:
    """Create a verbosity command-line option.

    This option can be used multiple times to increase the verbosity level of logging.
    Each occurrence of the option increases the logging verbosity level.

    Args:
        help_text: The help text for the command-line option.

    Returns:
        A Typer option configured for verbosity.
    """
    return TyperOption("-v", "--verbose", help=help_text, count=True)  # pyright: ignore[reportAny]


cli = typer.Typer(help="Main CLI for audiobookshelf-sdk.")
console = get_console()

# !devtools should be the last subcommand added to ensure it appears at the end of the help output.
cli.add_typer(devtools_cli, name="devtools", help="Developer tools for audiobookshelf-sdk.")


@cli.callback()
def main(
    ctx: ProjectContext,
    verbosity: Annotated[int, verbosity_option()] = 0,
    dry_run: Annotated[
        bool, typer.Option("-d", "--dry-run", help="Simulate actions without making changes.")
    ] = False,
) -> None:
    """Main entry point for the CLI, setting up global options and context."""
    ctx.obj = GlobalCLIOptions(verbosity=verbosity, dry_run=dry_run)


if __name__ == "__main__":
    cli()
