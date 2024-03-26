"""
Count at precisely 100 Hz.
"""
from timed_count import timed_count


for count in timed_count(1 / 100, error_on_missed=True):
    print(count)
