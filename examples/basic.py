"""
Count at half second time steps.
"""
from timed_count import timed_count


for count in timed_count(0.5):
    print(count)
