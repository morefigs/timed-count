"""
Count at precisely 100 Hz.
"""
from timed_count import timed_count, TimedCountError


for count in timed_count(0.01):
    print(count)

    if count.lag:
        raise TimedCountError('high iteration frequency could not be maintained')
