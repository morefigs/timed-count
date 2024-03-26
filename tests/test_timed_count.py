from time import sleep

import pytest
from pytest import approx

from timed_count import timed_count, CountMissedError


@pytest.mark.parametrize('period, start, stop', [
    (0.1, 0, 3),
    (0.1, 2, 5),
    (0.2, 0, 3),
])
@pytest.mark.parametrize('sleep_time', [
    0,
    0.05,
])
def test_timing(period: float, start: int, stop: int, sleep_time: float):
    abs_res = 0.02
    for i, count in enumerate(timed_count(period=period, start=start, stop=stop)):
        count_i = i + start
        time = count_i * period
        assert count.index == count_i
        assert count.count == time
        assert count.time == approx(time, abs=abs_res)
        if i == 0:
            assert count._time_ready == 0
            assert count.buffer == start * period
        else:
            assert count._time_ready == approx(time - period + sleep_time, abs=abs_res)
            assert count.buffer == approx(period - sleep_time, abs=abs_res)
        assert count.lag == approx(0, abs=abs_res)
        assert not count.missed

        # Add some iteration delay
        sleep(sleep_time)


def test_count_missed_error():
    with pytest.raises(CountMissedError):
        for _ in timed_count(0.01, stop=2, error_on_missed=True):
            sleep(0.1)
