"""
A module containing the ArchiveFile class.

Path: archive_strategy/archive_file.py

"""
import shutil
from datetime import datetime
from itertools import groupby
from pathlib import Path

from .console import logger


class ArchiveFile:
    """
    A class representing a backup file.

    Attributes:
    - path (Path): The path to the backup file.
    - parent (Archive): The parent archive.
    - config (ArchiveConfig): The archive configuration.
    - owner (str): The owner of the backup file.
    - group (str): The group of the backup file.
    - timeframe (Timeframe): The timeframe of the backup file.

    Methods:
    - name() -> str: Returns the name of the backup file.
    - timestamp() -> datetime: Returns the timestamp of the backup file.
    - age() -> str: Returns the age of the backup file in human readable format.
    - size() -> str: Returns the size of the backup file in human readable format.
    - to_delete() -> bool: Checks if the backup file should be deleted.
    - to_archive() -> bool: Checks if the backup file should be moved to the archive.
    - update_owner() -> bool: Checks if the owner of the backup file should be updated.
    - change_owner(): Changes the owner of the backup file.
    - move_to_archive(): Moves the backup file to the archive.
    - apply_policy(): Applies the policy to the backup file.
    - cleanup(): Cleans up the archive directory.
    - _should_keep() -> bool: Checks if the backup file should be kept.
    - get_frame_group_key(): Returns the frame group key.
    """

    def __init__(self, path, parent) -> None:
        self.path = Path(path)
        self.parent = parent
        self.config = parent.config
        self.owner = self.path.owner()
        self.group = self.path.group()
        self.timeframe = None

    @property
    def name(self) -> str:
        """Return the name of the backup file."""
        return self.path.name

    @property
    def timestamp(self) -> datetime:
        """Return the timestamp of the backup file."""
        try:
            first_part = self.name.split("_")[0]
            timestamp = datetime.fromtimestamp(int(first_part))
        except ValueError:
            timestamp = datetime.fromtimestamp(self.path.stat().st_mtime)
        return timestamp

    @property
    def age(self) -> str:
        """Return the age of the file in human readable format: 1m 2w 2d 3h 5m"""
        age = datetime.now() - self.timestamp
        days = age.days
        hours, remainder = divmod(age.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        weeks, days = divmod(days, 7)
        age = f"{weeks}w {days}d {hours}h {minutes}m"
        return age

    @property
    def size(self) -> str:
        """Get the size of the file in human readable format: example: 1.2 GB"""
        if not self.path.exists():
            return "Missing"
        bytesize = self.path.stat().st_size

        file_size_megabytes = bytesize / (1024 * 1024)
        file_size_gigabytes = bytesize / (1024 * 1024 * 1024)

        if file_size_gigabytes > 1:
            size = f"{file_size_gigabytes:.2f} GB"
        elif file_size_megabytes > 1:
            size = f"{file_size_megabytes:.2f} MB"
        else:
            size = f"{bytesize} bytes"

        return size

    @property
    def to_delete(self) -> bool:
        """Check if the file should be deleted."""
        if not self.config.prune or not self.timeframe or self.timeframe.keep == "all":
            return False
        if self.timeframe.keep == "none":
            return True
        if self.timeframe.keep == "latest":
            if self == self.parent.files[0]:
                return False
            return True

        if isinstance(self.timeframe.keep, int):
            return self._should_keep()

        return False

    @property
    def to_archive(self) -> bool:
        """If the source directory is not the same as the destination directory,
        the backup file should be moved into the archive."""
        if self.config.source == self.config.destination:
            return False
        if self.path.parent == self.config.source:
            return True
        return False

    @property
    def update_owner(self) -> bool:
        """Update the owner of the backup file, but only if the owner is not the same
        as the owner passed through the archive configuration.
        """
        if self.config.owner is None:
            return False
        if self.owner != self.config.owner:
            return True
        return False

    def change_owner(self) -> None:
        """Change the owner of the backup file to the owner passed through the archive
        configuration.
        """
        if self.update_owner:
            shutil.chown(self.path, self.config.owner, self.config.group)
            logger.log(f"Changed owner of {self.path.name} to {self.config.owner}")

    def move_to_archive(self) -> None:
        """Move the backup to the archive directory."""
        if self.to_archive:
            if not self.config.destination.exists():
                self.config.destination.mkdir(parents=True)
            target_location = self.config.destination / self.name
            self.path = self.path.replace(target_location)

    def apply_policy(self) -> None:
        """Check which policy applies to the backup and apply it."""
        for timeframe in self.config.policy.timeframes:
            if timeframe.start < self.timestamp < timeframe.end:
                self.timeframe = timeframe
                break

    def cleanup(self, progress) -> None:
        """Cleanup the archive directory."""
        if self.config.prune and self.to_delete:
            self.path.unlink()
            progress.console.print(f"Deleted {self.path.name}")

    def _should_keep(self) -> bool:
        """Check if the backup should be kept based on the timeframe and the number
        of backups in the same timeframe. If the position of the backup in the list
        of backups in the same timeframe is higher than the number of backups to keep,
        the backup should be deleted.
        """

        # If keep is 0, no backups should be kept
        if self.timeframe.keep == 0:
            return True

        if self.timeframe.keep >= 1:
            if len(self.parent.files) == 1:
                return False

            # Get all backups in the same timeframe
            timeframe_backups = filter(
                lambda b: b.timeframe.frame == self.timeframe.frame, self.parent.files
            )
            # Sort the backups by timestamp (newest first)
            timeframe_backups = sorted(timeframe_backups, reverse=True)

            # Group the backups by frame group key
            grouped_backups = groupby(
                timeframe_backups, key=lambda b: b.get_frame_group_key()
            )

            for _, files in grouped_backups:
                file_list = list(files)
                if self not in file_list:
                    continue
                if file_list.index(self) > self.timeframe.keep - 1:
                    return True
            return False

        return False

    def get_frame_group_key(self):
        """Return the frame group key. This key is used to group backups by frame."""
        if self.timeframe.frame == "hours":
            return self.timestamp.hour
        if self.timeframe.frame == "days":
            return self.timestamp.date()
        if self.timeframe.frame == "weeks":
            return self.timestamp.isocalendar()[1]
        if self.timeframe.frame == "months":
            return self.timestamp.month
        if self.timeframe.frame == "years":
            return self.timestamp.year
        raise ValueError(f"Invalid frame grouping key: {self.timeframe.frame}")

    def __repr__(self) -> str:
        """
        Return a string representation of the ArchiveFile object.

        :return: String representation of the ArchiveFile object
        :rtype: str
        """
        return f"ArchiveFile({self.size}, age={self.age})"

    def __lt__(self, other) -> bool:
        """
        Compare two ArchiveFile objects using the '<' operator.

        :param other: Another ArchiveFile object
        :return: True if the first backup is older than the second backup

        """
        return self.timestamp < other.timestamp

    def __gt__(self, other) -> bool:
        """
        Compare two ArchiveFile objects using the '>' operator.

        :param other: Another ArchiveFile object
        :return: True if the first backup is newer than the second backup

        """
        return self.timestamp > other.timestamp

    def __eq__(self, other) -> bool:
        """
        Compare two ArchiveFile objects using the '==' operator.

        :param other: Another ArchiveFile object
        :return: True if the first backup is equal to the second backup

        """
        return self.path == other.path

    def __hash__(self) -> int:
        return hash(self.path)

    def __or__(self, other) -> set:
        """
        Concatenate two ArchiveFile objects using the '|' operator.

        :param other: Another ArchiveFile object
        :return: A dictionary containing the concatenated backups

        """
        return {self, other}

    def __add__(self, other) -> set:
        """
        Concatenate two ArchiveFile objects using the '+' operator.

        :param other: Another ArchiveFile object
        :return: A dictionary containing the concatenated backups

        """
        return {self, other}

    def __iter__(self) -> iter:
        """
        Return an iterator over the ArchiveFile object.

        :return: Iterator over the ArchiveFile object

        """
        yield self
