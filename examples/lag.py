"""
Count at half second time steps that are delayed by slow code execution, stopping when the cumulative lag exceeds half a
second.
"""
from time import sleep

from timed_count import timed_count, TimedCountError


for count in timed_count(0.5):
    print(count)

    if count.lag > 0.5:
        raise TimedCountError('timed count lagged too much')

    # Wait longer than the count period!
    sleep(0.6)
