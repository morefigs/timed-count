from pytest import approx

from timed_count import TimedCount


class TestTimedCount:
    def test_init(self):
        count = TimedCount(1, count=2.0, time=3.0, _time_ready=4.0, _count_dp=5, _time_dp=6)
        assert count.index == 1
        assert count.count == approx(2.0)
        assert count.time == approx(3.0)
        assert count._time_ready == approx(4.0)
        assert count._count_dp == 5
        assert count._time_dp == 6

    def test_repr(self):
        assert repr(TimedCount(1, count=2.34, time=2.345, _time_ready=0.0, _count_dp=2, _time_dp=3)) == \
               'TimedCount(index=1, count=2.34, time=2.345, missed=False)'

    def test_buffer(self):
        assert TimedCount(0, count=0.0, time=0.0, _time_ready=0.0, _count_dp=1, _time_dp=1).buffer == 0
        assert TimedCount(0, count=1.0, time=1.0, _time_ready=0.1, _count_dp=1, _time_dp=1).buffer == approx(0.9)

        # Delayed time results in 0 buffer
        assert TimedCount(0, count=1.0, time=1.1, _time_ready=1.1, _count_dp=1, _time_dp=1).buffer == 0

    def test_lag(self):
        assert TimedCount(0, count=1.0, time=1.0, _time_ready=0.0, _count_dp=1, _time_dp=1).lag == 0
        assert TimedCount(0, count=1.0, time=1.1, _time_ready=1.1, _count_dp=1, _time_dp=1).lag == approx(0.1)

    def test_missed(self):
        assert TimedCount(0, count=1.0, time=1.0, _time_ready=0.0, _count_dp=1, _time_dp=1).missed is False
        assert TimedCount(0, count=1.0, time=1.1, _time_ready=1.1, _count_dp=1, _time_dp=1).missed is True
