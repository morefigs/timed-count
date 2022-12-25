"""
Count while occasionally delaying the next iteration, which results in the `missed` attribute returning `True`.
"""
from time import sleep
from random import random

from timed_count import timed_count


for count in timed_count(0.75):
    print(count)
    sleep(random())
