"""
Count at precisely 100 Hz.
"""
from timed_count import timed_count, CountDelayedError


for count in timed_count(1 / 100):
    print(count)

    if count.delayed:
        raise CountDelayedError('high iteration frequency could not be maintained')
