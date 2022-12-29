# timed-count

**timed-count** provides an iterator that delays each iteration by a specified time period. It can be used to repeatedly  execute code at a precise frequency.

**timed-count** is a good replacement for a loop that contains a call to `time.sleep`. It is precise, does not dependent on the loop execution time, and won't accumulate temporal drift.

## Installation

Install from [PyPI](https://pypi.org/project/timed-count/) via:

```shell
pip install timed-count
```

## Usage

Basic usage is as follows:

```python
from timed_count import timed_count

for count in timed_count(0.5):
    # Prints at exactly every half a second
    print(count)
```

```python
TimedCount(index=0, count=0.0, time=0.000, missed=False)
TimedCount(index=1, count=0.5, time=0.500, missed=False)
TimedCount(index=2, count=1.0, time=1.000, missed=False)
...
```
For all usage examples see [examples/](https://github.com/morefigs/timed-count/tree/main/examples).
