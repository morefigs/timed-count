from dataclasses import dataclass


@dataclass(frozen=True)
class TimedCount:
    period: float
    index: int
    time: float
    _time_ready: float

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(index={self.index}, time={self.time:.03f}, lag={self.lag:.03f})'

    @property
    def count(self) -> float:
        """
        The nominal count time, in seconds since timed_count was called.
        """
        return self.period * self.index

    @property
    def buffer(self) -> float:
        """
        The length of time before the nominal count time that the count was requested. The minimum buffer is zero.
        """
        return max(0.0, self.count - self._time_ready)

    @property
    def lag(self) -> float:
        """
        The length of time after the nominal count time that the count was requested. The minimum lag is zero.

        If the lag is non-zero, then the code executed since the previous count took longer than the count period, which
        is generally undesirable.
        """
        return self.time - self.count

    @property
    def delayed(self) -> bool:
        if self.index:
            return not self.buffer

        # Define index of 0 as never delayed
        return False


# Catch all error class for all package related errors
class TimedCountError(Exception):
    pass


class CountDelayedError(TimedCountError):
    pass
