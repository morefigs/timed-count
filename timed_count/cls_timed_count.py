from dataclasses import dataclass


@dataclass(frozen=True)
class TimedCount:
    period: float
    index: int
    count: float
    time: float
    _time_ready: float
    _count_dp: int
    _time_dp: int

    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}(index={self.index}, count={self.count:.{self._count_dp}f}, '
                f'time={self.time:.{self._time_dp}f}, lag={self.lag:.{self._time_dp}f})')

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

        To check if the iteration was actually missed by the caller, check the `missed` attribute.
        """
        return self.time - self.count

    @property
    def missed(self) -> bool:
        """
        Shows if this iteration was requested after the nominal count time.
        """
        return self._time_ready > self.count


# Catch all error class
class TimedCountError(Exception):
    pass


class CountDelayedError(TimedCountError):
    pass
