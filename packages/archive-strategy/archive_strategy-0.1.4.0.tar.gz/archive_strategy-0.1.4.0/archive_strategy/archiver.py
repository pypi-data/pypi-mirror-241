"""The Archiver class is responsible for archiving files based on a set of policies."""
from rich.progress import Progress
from rich.table import Table

from .archive_file import ArchiveFile
from .config import ArchiveConfig
from .console import logger


class Archiver:
    """
    The Archiver class is responsible for archiving files based on a set of policies.

    Args:
        config (ArchiveConfig): An instance of ArchiveConfig containing the
            configuration for the archiver.

    Attributes:
        config (ArchiveConfig): An instance of ArchiveConfig containing the
            configuration for the archiver.
        files (list): A list of ArchiveFile instances representing the files to be
            archived.
    """

    def __init__(self, config: ArchiveConfig) -> None:
        self.config = config
        self.files = []
        self._gather_files()

    def _gather_files(self) -> None:
        """Gather all files from both source and destination directory."""
        files = set()
        for archive_file in self.config.source.rglob("*.gz"):
            files.add(ArchiveFile(archive_file, self))

        # When the archive directory is not a subdirectory of the source directory,
        # also gather the files from the archive directory
        for archive_file in self.config.destination.rglob("*.gz"):
            files.add(ArchiveFile(archive_file, self))

        # Sort the files by timestamp (newest first)
        self.files = sorted(files, reverse=True)

    def list_files(
        self,
        full_path: bool = False,
        timeframe: bool = False,
        to_move: bool = False,
        to_prune: bool = False,
    ) -> None:
        """List the files that will be archived.

        Args:
            full_path (bool, optional): Whether to show the full path or just the file
                name. Defaults to False.
            timeframe (bool, optional): Whether to show the timeframe of the file.
                Defaults to False.
            to_move (bool, optional): Whether to show whether the file will be moved to
                the archive directory. Defaults to False.
            to_prune (bool, optional): Whether to show whether the file will be deleted
                after archiving. Defaults to False.

        Returns:
            None
        """

        table = Table(title="Archive")
        table.add_column("File Name")
        table.add_column("Size", justify="right")
        table.add_column("Age", justify="right", style="green")
        if timeframe:
            table.add_column("Timestamp", style="magenta")
            table.add_column("Timeframe", style="cyan")
            table.add_column("Timeframe Key", style="cyan")
        if to_move:
            table.add_column("Move to Archive", justify="right", style="blue")
        if to_prune:
            table.add_column("Remove", style="red")

        for archive_file in self.files:
            row = [
                archive_file.path.absolute().as_posix()
                if full_path
                else archive_file.path.name,
                archive_file.size,
                archive_file.age,
            ]

            if timeframe:
                row.append(archive_file.timestamp.strftime("%Y-%m-%d %H:%M"))
                row.append(
                    str(archive_file.timeframe) if archive_file.timeframe else "TBD"
                )
                row.append(
                    str(archive_file.get_frame_group_key())
                    if archive_file.timeframe
                    else "TBD"
                )
            if to_move:
                row.append("Yes" if archive_file.to_archive else "No")
            if to_prune:
                row.append("Yes" if archive_file.to_delete else "No")
            table.add_row(*row)

        logger.print(table)

    def apply_policies_to_files(self) -> None:
        """Apply the retention policies to the files."""
        for archive_file in self.files:
            archive_file.apply_policy()

    def archive(self) -> None:
        """Main method to archive the files."""
        self._gather_files()
        self.apply_policies_to_files()

        files_to_archive = [f for f in self.files if f.to_archive]
        files_to_change_owner = [f for f in self.files if f.update_owner]
        files_to_delete = [f for f in self.files if f.to_delete]

        with Progress() as progress:
            move_task = progress.add_task(
                "Moving to archive...", total=len(files_to_archive)
            )
            owner_task = progress.add_task(
                "Changing owner...", total=len(files_to_change_owner)
            )
            prune_task = progress.add_task(
                "Pruning files...", total=len(files_to_delete)
            )

            for archive_file in files_to_archive:
                archive_file.move_to_archive()
                to_advance = (
                    1 / len(files_to_archive) if len(files_to_archive) > 0 else 1
                )
                progress.advance(move_task, advance=to_advance)

            for archive_file in files_to_change_owner:
                archive_file.change_owner()
                to_advance = (
                    1 / len(files_to_change_owner)
                    if len(files_to_change_owner) > 0
                    else 1
                )
                progress.advance(owner_task, advance=to_advance)

            for archive_file in files_to_delete:
                archive_file.cleanup(progress)
                to_advance = 1 / len(files_to_delete) if len(files_to_delete) > 0 else 1
                progress.advance(prune_task, advance=to_advance)
