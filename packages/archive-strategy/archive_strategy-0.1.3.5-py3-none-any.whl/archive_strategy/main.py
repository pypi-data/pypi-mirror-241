import click
from rich.console import Console
from rich.theme import Theme

from .archiver import Archiver
from .config import ArchiveConfig

archiver_theme = Theme({"info": "dim cyan", "warning": "magenta", "danger": "bold red"})
logger = Console(theme=archiver_theme, width=250)


@click.group()
def config():
    pass


@config.command()
def show_config():
    """Show the current configuration"""
    archive_config = ArchiveConfig()
    archive_config._show()


@click.group()
def information():
    pass


@information.command()
@click.option(
    "--show-all",
    is_flag=True,
    show_default=True,
    help="Show all information about the file.",
)
@click.option(
    "--show-full-path",
    is_flag=True,
    show_default=True,
    help="Show the full path of the file.",
)
@click.option(
    "--show-timestamp",
    is_flag=True,
    show_default=True,
    help="Show the timestamp of the file.",
)
@click.option(
    "--show-timeframe",
    is_flag=True,
    show_default=True,
    help="Show the timeframe of the file.",
)
@click.option(
    "--show-timeframe-key",
    is_flag=True,
    show_default=True,
    help="Show the timeframe key of the file.",
)
@click.option(
    "--show-to-move",
    is_flag=True,
    show_default=True,
    help="Show whether the file will be moved to the archive.",
)
@click.option(
    "--show-to-prune",
    is_flag=True,
    show_default=True,
    help="Show whether the file will be pruned.",
)
def show(
    show_all,
    show_full_path,
    show_timestamp,
    show_timeframe,
    show_timeframe_key,
    show_to_move,
    show_to_prune,
):
    """Show the current list of backups"""
    archive_config = ArchiveConfig()
    archiver = Archiver(config=archive_config)
    archiver.apply_policies_to_files()

    # If the user specifies --all, show all information
    if all:
        show_full_path = True
        show_timestamp = True
        show_timeframe = True
        show_timeframe_key = True
        show_to_move = True
        show_to_prune = True

    archiver.list_files(
        full_path=show_full_path,
        timestamp=show_timestamp,
        timeframe=show_timeframe,
        timeframe_key=show_timeframe_key,
        to_move=show_to_move,
        to_prune=show_to_prune,
    )


@click.group()
def execution():
    pass


@execution.command()
@click.option(
    "--prune",
    is_flag=True,
    default=None,
    show_default=True,
    help="Determine whether to prune backup files that are no longer needed.",
)
@click.option(
    "--verbose",
    is_flag=True,
    default=False,
    show_default=True,
    help="Display additional information for debugging.",
)
def run(prune, verbose):
    """Run the archiver"""
    archive_config = ArchiveConfig(prune=prune, verbose=verbose)
    archiver = Archiver(config=archive_config)
    archiver.apply_policies_to_files()
    archiver.archive()


cli = click.CommandCollection(sources=[config, information, execution])


def main():
    cli()
