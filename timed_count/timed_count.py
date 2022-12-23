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
                temporal_resolution_exponent: int = -4) -> Iterator[TimedCount]:
    """
    `timed-count` is a generator function that returns an iterator that delays each iteration by the specified time
    period. It can be used to execute code at a precise frequency.
    :param period: The interval period, in seconds.
    :param start: The number of time counts to delay starting by.
    :param stop: The number of time counts to automatically stop after.
    :param temporal_resolution_exponent: The temporal resolution exponent to use when blocking the next iteration. A
    lower value will give higher resolution and precision but result in higher CPU usage. Use caution lowering below the
    default value. This precision is for an individual iteration only, there is no cumulative time error over multiple
    iterations.
    """
    index = start

    # E.g. 10 ** -4 = 0.0001
    cpu_sleep_s = 10 ** temporal_resolution_exponent

    # count decimal places matches period decimal places
    count_dp = max(1, -Decimal(str(period)).as_tuple().exponent)

    # time decimal places one less than temporal resolution
    time_dp = max(count_dp, -temporal_resolution_exponent - 1)

    with Stopwatch() as stopwatch:
        while True:
            if stop is not None and index >= stop:
                return

            # Starts the stopwatch on first call, so first call returns exactly 0
            time_ready = stopwatch.time(True)
            time = time_ready

            # Block the iteration until the next count time
            count = period * index
            while time < count:
                sleep(cpu_sleep_s)
                time = stopwatch.time()

            timed_count_ = TimedCount(period, index, time, time_ready, count_dp, time_dp)
            index += 1

            yield timed_count_
