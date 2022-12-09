# timed-count

`timed-count` is a generator function that returns an iterator that delays each iteration by the specified time period. It can be used to execute code at a precise frequency.

`timed-count` is a good replacement for a loop that contains a `time.sleep` call. It is precise, does not dependent on the loop execution time, and won't accumulate temporal drift.

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

For all usage examples see [examples/](https://github.com/morefigs/timed-count/tree/main/examples).
