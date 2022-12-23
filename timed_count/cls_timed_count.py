from dataclasses import dataclass


@dataclass(frozen=True)
class TimedCount:
    period: float
    index: int
    time: float
    _time_ready: float
    _count_dp: int
    _time_dp: int

    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}(index={self.index}, count={self.count:.{self._count_dp}f}, '
                f'time={self.time:.{self._time_dp}f}, lag={self.lag:.{self._time_dp}f})')

    @property
    def count(self) -> float:
        """
        The nominal count time, in seconds since timed_count was called.
        """
        return self.period * self.index

    @property
    def buffer(self) -> float:
        """
        The length of time before the nominal count time that the iteration was requested. The minimum buffer is zero.
        """
        return max(0.0, self.count - self._time_ready)

    @property
    def lag(self) -> float:
        """
        The length of time after the nominal count time that the iteration was yielded. The lag is always at least
        slightly above zero due to delays from internal code execution.

        To check if the iteration was actually delayed by the caller, check the `delayed` attribute.
        """
        return self.time - self.count

    @property
    def delayed(self) -> bool:
        """
        Shows if this iteration was requested after the nominal count time.
        """
        if self.index:
            return not self.buffer

        # Define index of 0 as never delayed
        return False


# Catch all error class for all package related errors
class TimedCountError(Exception):
    pass


class CountDelayedError(TimedCountError):
    pass
