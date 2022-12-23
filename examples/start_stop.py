"""
Count at quarter second time steps, delaying by 4 counts and stopping after 8 counts (including those skipped).
"""
from timed_count import timed_count


for count in timed_count(0.25, start=4, stop=8):
    print(count)
