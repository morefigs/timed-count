from __future__ import annotations
from typing import Optional
from collections.abc import Iterator
from time import sleep
from decimal import Decimal

from stoppy import Stopwatch

from timed_count.cls_timed_count import TimedCount


def timed_count(period: float,
                start: int = 0,
                stop: Optional[int] = None,
                temporal_resolution: float = 0.0001) -> Iterator[TimedCount]:
    """
    A generator function that returns  an iterator that delays each iteration by a specified time period. It can be used
    to repeatedly execute code at a precise frequency.
    :param period: The interval period, in seconds.
    :param start: The number of time counts to delay starting by.
    :param stop: The number of time counts to automatically stop after.
    :param temporal_resolution: The temporal resolution (or time error) to use when waiting for the next iteration, in
    seconds. A smaller value will give higher resolution and precision but result in higher CPU usage. Use caution
    lowering below the default value. This precision is for an individual iteration only, there is no cumulative time
    error over multiple iterations.
    """
    index = start

    # `count` decimal places matches period decimal places
    count_dp = max(1, -Decimal(str(period)).as_tuple().exponent)

    # `time` decimal places one less than temporal resolution
    time_dp = max(count_dp, -Decimal(str(temporal_resolution)).as_tuple().exponent - 1)

    with Stopwatch() as stopwatch:
        while True:
            if stop is not None and index >= stop:
                return

            count = period * index

            # Starts the stopwatch on first call, so first call returns exactly 0
            time_ready = stopwatch.time(True)

            # Block the iteration until the next count time
            time = stopwatch.time()
            while time < count:
                sleep(temporal_resolution)
                time = stopwatch.time()

            yield TimedCount(index, count, time, time_ready, count_dp, time_dp)

            index += 1
