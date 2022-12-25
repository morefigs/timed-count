from dataclasses import dataclass


@dataclass(frozen=True)
class TimedCount:
    """
    TimedCount object that represents the timed count for a single iteration.
    :param index: The index of the count.
    :param count: The nominal count time, in seconds since timed_count was called.
    :param time: The actual count time, in seconds since timed_count was called.
    :param _time_ready: The time this iteration was initially requested.
    :param _count_dp: Decimal places to represent the `count` value with as a string.
    :param _time_dp: Decimal places to represent the `time` value with as a string.
    """
    index: int
    count: float
    time: float
    _time_ready: float
    _count_dp: int
    _time_dp: int

    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}(index={self.index}, count={self.count:.{self._count_dp}f}, '
                f'time={self.time:.{self._time_dp}f}, missed={self.missed})')

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


class CountMissedError(TimedCountError):
    pass
