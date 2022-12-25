"""
Count at precisely 100 Hz.
"""
from timed_count import timed_count, CountMissedError


for count in timed_count(1 / 100):
    print(count)

    if count.missed:
        raise CountMissedError('high iteration frequency could not be maintained')
