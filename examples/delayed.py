"""
Count at half second time steps, occasionally delaying the next iteration.
"""
from time import sleep
from random import uniform

from timed_count import timed_count


for count in timed_count(0.5):
    # The `lag` attribute is never exactly 0, so use `delayed` attribute to check for slow code execution
    print(count, f'delayed={count.delayed}')

    sleep(uniform(0.4, 0.6))
