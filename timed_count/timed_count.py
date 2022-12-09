from __future__ import annotations
from typing import Optional
from collections.abc import Iterator
from time import sleep

from stoppy import Stopwatch

from timed_count.timed_count_cls import TimedCount, TimedCountError


# Affects timer precision, but also prevents high CPU usage
_CPU_SLEEP_S = 0.0001


def timed_count(period: float, start: int = 0, stop: Optional[int] = None) -> Iterator[TimedCount]:
    """
    `timed-count` is a generator function that returns an iterator that delays each iteration by the specified time
    period. It can be used to execute code at a precise frequency.
    :param period: The interval period, in seconds.
    :param start: The number of time counts to delay starting by.
    :param stop: The number of time counts to automatically stop after.
    """
    count = start

    with Stopwatch() as stopwatch:
        while True:
            if stop is not None and count >= stop:
                return

            # Starts the stopwatch on first call, guaranteeing that the first call of stopwatch.time returns 0
            timed_count_ = TimedCount(period, count, stopwatch.time(True))
            count += 1

            # Block the iteration until the next count time
            while stopwatch.time() < timed_count_.time:
                sleep(_CPU_SLEEP_S)

            yield timed_count_
