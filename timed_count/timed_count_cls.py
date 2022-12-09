from dataclasses import dataclass


@dataclass
class TimedCount:
    period: float
    count: int
    _time_ready: float

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(count={self.count}, time={self.time:.03f}, lag={self.lag:.03f})'

    @property
    def time(self) -> float:
        """
        The count time, in seconds since timed_count was called.
        """
        return self.count * self.period

    @property
    def buffer(self) -> float:
        """
        The length of time before the nominal count time that the count was requested. The minimum buffer is zero.
        """
        if self.time < self._time_ready:
            return 0
        return self.time - self._time_ready

    @property
    def lag(self) -> float:
        """
        The length of time after the nominal count time that the count was requested. The minimum lag is zero.

        If the lag is non-zero, then the code executed since the previous count took longer than the count period, which
        is generally undesirable.
        """
        if self._time_ready < self.time:
            return 0
        return self._time_ready - self.time


class TimedCountError(Exception):
    pass
