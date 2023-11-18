from datetime import datetime

from dateutil.relativedelta import relativedelta


class Timeframe:
    def __init__(self, frame: str, count: int, keep: str = "all"):
        self.frame = frame
        self.count = count
        self.keep = keep

    @property
    def start(self):
        return datetime.now() - relativedelta(**{self.frame: self.count})

    @property
    def end(self):
        return datetime.now()

    def __str(self):
        return f"Frame: {self.frame}, Count: {self.count}, Keep: {self.keep}"

    def __repr__(self):
        return self.__str()

    def applies(self, timestamp):
        return self.start < timestamp < self.end
