from __future__ import annotations
from typing import Optional
from collections.abc import Iterator
from time import sleep

from stoppy import Stopwatch

from timed_count.cls_timed_count import TimedCount, TimedCountError


def timed_count(period: float,
                start: int = 0,
                stop: Optional[int] = None,
                temporal_resolution: float = 0.0001) -> Iterator[TimedCount]:
    """
    `timed-count` is a generator function that returns an iterator that delays each iteration by the specified time
    period. It can be used to execute code at a precise frequency.
    :param period: The interval period, in seconds.
    :param start: The number of time counts to delay starting by.
    :param stop: The number of time counts to automatically stop after.
    :param temporal_resolution: The approximate maximum temporal resolution (or time error) for each iteration, in
    seconds. A smaller temporal resolution value will result in a smaller time error and higher precision. However,
    decreasing this value below the default value will begin to significantly increase CPU usage. This time error is for
    an individual iteration only, there is no cumulative time error over multiple iterations.
    """
    index = start

    with Stopwatch() as stopwatch:
        while True:
            if stop is not None and index >= stop:
                return

            # Starts the stopwatch on first call, guaranteeing that the first call of stopwatch.time returns 0
            timed_count_ = TimedCount(period, index, stopwatch.time(True))
            index += 1

            # Block the iteration until the next count time
            while stopwatch.time() < timed_count_.time:
                sleep(temporal_resolution)

            yield timed_count_
