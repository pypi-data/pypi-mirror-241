"""Timeframe class."""
from datetime import datetime

from dateutil.relativedelta import relativedelta


class Timeframe:
    """
    A class representing a timeframe.

    Attributes:
        - frame (str): The frame of the timeframe.
        - count (int): The count of the timeframe.
        - keep (str): The keep of the timeframe.

    """

    def __init__(self, frame: str, count: int, keep: str = "all"):
        self.frame = frame
        self.count = count
        self.keep = keep

    @property
    def start(self):
        """Start of the timeframe."""
        return datetime.now() - relativedelta(**{self.frame: self.count})

    @property
    def end(self):
        """End of the timeframe. Which is basically now."""
        return datetime.now()

    def __str(self):
        return f"Frame: {self.frame}, Count: {self.count}, Keep: {self.keep}"

    def __repr__(self):
        return self.__str()

    def applies(self, timestamp: datetime) -> bool:
        """Check if the timeframe applies to the timestamp.

        :param timestamp: Timestamp to check
        """
        return self.start < timestamp < self.end
