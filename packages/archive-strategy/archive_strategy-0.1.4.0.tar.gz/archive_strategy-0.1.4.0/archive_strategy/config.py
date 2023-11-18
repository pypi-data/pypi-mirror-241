"""A module for the configuration of the archiver."""
import tomllib
from pathlib import Path

from rich.columns import Columns

from .console import logger
from .policy import ArchivePolicy


class ArchiveConfig:  # pylint: disable=too-many-instance-attributes
    """A class representing the configuration for the archiver."""

    def __init__(
        self, source=None, destination=None, **kwargs
    ):  # pylint: disable=too-many-locals
        data = self._load_configuration_file()

        source_path = source or data["config"].get("source")
        self.source = Path(source_path) if source_path else Path.cwd()

        destination_path = destination or data["config"].get("destination")
        self.destination = (
            Path(destination_path) if destination_path else self.source / "archive"
        )

        dry_run = data["config"].get("dry_run", True)
        self.dry_run = kwargs.get("dry_run", dry_run)

        verbose = data["config"].get("verbose", False)
        self.verbose = kwargs.get("verbose", verbose)

        prune = data["config"].get("prune", False)
        self.prune = kwargs.get("prune", prune)

        owner = data["config"].get("owner")
        self.owner = kwargs.get("owner", owner)

        group = data["config"].get("group")
        self.group = kwargs.get("group", group)

        if kwargs.get("policies"):
            self.policy = ArchivePolicy(kwargs.get("policies"))
        else:
            policies = data.get("policies", {})
            policy_vals = []
            for frame, values in policies.items():
                if isinstance(values, dict):
                    policy_vals.append(
                        {
                            "type": frame,
                            "count": values["count"],
                            "keep": values["keep"],
                        }
                    )
                elif isinstance(values, list):
                    for value in values:
                        policy_vals.append(
                            {
                                "type": frame,
                                "count": value["count"],
                                "keep": value["keep"],
                            }
                        )
            self.policy = ArchivePolicy(policy_vals)

    def __str__(self):
        return f"ArchiveConfig(source={self.source}, destination={self.destination})"

    def __repr__(self):
        return self.__str__()

    def _load_configuration_file(self):
        """Load the configuration from a TOML file if it exists.

        Acceptable config file locations:
        - /etc/archive_strategy.toml
        - ~/.archive_strategy.toml
        - ./archive_strategy.toml

        """
        data = {}
        for path in [
            Path("/etc/archive_strategy.toml"),
            Path.home() / ".archive_strategy.toml",
            Path.cwd() / "archive_strategy.toml",
        ]:
            if path.exists():
                try:
                    data = tomllib.loads(path.read_text(encoding="utf-8"))
                except Exception as e:
                    raise ValueError(f"Invalid TOML file: {path}. Error: {e}") from e

        if not data.get("config"):
            data["config"] = {}

        return data

    def log_to_console(self):
        """Log the configuration to the console in a verbose format."""
        headers = [
            "Source",
            "Destination",
            "Dry Run",
            "Verbose",
            "Prune",
            "Owner",
            "Group",
        ]
        values = [
            self.source,
            self.destination,
            self.dry_run,
            self.verbose,
            self.prune,
            self.owner,
            self.group,
        ]
        left = "\n".join(f"[info]{x}:[/info]" for x in headers)
        right = "\n".join(str(x) for x in values)
        columns = Columns([left, right], equal=True)
        logger.print(columns)
