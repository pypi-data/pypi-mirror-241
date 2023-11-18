"""
Defines the retention policy of a file..
"""
from .timeframe import Timeframe


class ArchivePolicy:
    """A strategy defines the retention policy of a backup.

    A retention policy can be defined in multiple ways. Either by specifying the number
    of backups to keep or by specifying the number of days to keep backups.

    The latter can also be combined with the number of backups to keep. For example, if
    you want to keep 3 days of backups regardless of the number of backups, you can
    specify the following:
    [
        {
            "type": "days",
            "count": 3,
        },
        {
            "type": "weeks",
            "count": 1,
        },
        {
            "type": "months",
            "count": 1,
        },
        {
            "type": "years",
            "count": 1,
        },
    ]

    The above list is interpreted as follows:
    - Keep 3 days of backups, regardless of the number of backups
    - Anything older than 3 days, Keep for 1 week, regardless of the number of backups
    - Anything older than 1 week, Keep for 1 month, regardless of the number of backups
    - Anything older than 1 month, Keep for 1 year, regardless of the number of backups

    When a backup moves from one retention policy to another, it is moved to a different
    directory. For example, if a backup is older than 3 days, it will be moved to the
    weekly directory. If a backup is older than 1 week, it will be moved to the monthly
    directory. If a backup is older than 1 month, it will be moved to the yearly
    directory.

    You can also specify the number of backups to keep. For example, if you want to keep
    1 backup for 4 weeks, you can specify the following:
    [
        {
            "type": "weeks",
            "count": 3,
            "keep": 1,
        },
    ]

    Note that the "keep" parameter is optional. If you don't specify it, all backups
    will be kept.

    Also note that the policies are cumulative. If you specify the following:
    [
        {
            "type": "weeks",
            "count": 3,
            "keep": 1,
        },
        {
            "type": "months",
            "count": 1,
            "keep": 1,
        },
    ]

    Then the following will happen:
    - Keep 1 backup for 3 weeks
    - Keep 1 backup for 1 month
    - Anything older than 1 month will be deleted.

    """

    def __init__(self, data=None):
        if data is None or (isinstance(data, list) and len(data) == 0):
            data = [{"type": "days", "count": 1}]
        self._data = data
        self._validate_policy()
        self._timeframes = self.get_timeframes()

    def _validate_policy(self):
        """Validate the policy."""
        if not isinstance(self._data, list):
            raise ValueError(
                f"Invalid retention policy definition. Expected a list, got "
                f"{type(self._data)}"
            )
        for frame in self._data:
            if not isinstance(frame, dict):
                raise ValueError(
                    f"Invalid retention policy item: {frame}. Expected a dictionary, "
                    f"got {type(frame)}"
                )
            if frame["type"] not in ["days", "weeks", "months", "years"]:
                raise ValueError(
                    f"Invalid retention policy. Type {frame['type']} is not "
                    f"supported."
                )
            if frame["count"] < 0:
                raise ValueError(
                    "Invalid retention policy. Count must be greater or equal to 0."
                )
            if "keep" in frame:
                if frame["keep"] != "all" and frame["keep"] < 0:
                    raise ValueError(
                        "Invalid retention policy. Keep must be greater than 0."
                    )

    def get_timeframes(self):
        """Return a list of start and end datetime objects for each timeframe."""
        timeframes = []
        for policy in self._data:
            values = {
                "frame": policy["type"],
                "count": policy["count"],
            }
            if "keep" in policy:
                values["keep"] = policy["keep"]

            timeframes.append(Timeframe(**values))

        # Always add a "to remove" timeframe which goes back to very far
        timeframes.append(Timeframe("years", 100, keep="none"))

        return timeframes

    @property
    def timeframes(self):
        """Return a list of start and end datetime objects for each timeframe."""
        for timeframe in self._timeframes:
            yield timeframe
