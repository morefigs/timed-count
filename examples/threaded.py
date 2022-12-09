"""
Count asynchronously in a dedicated thread.
"""
from threading import Thread, current_thread

from timed_count import timed_count


def threaded():
    for count in timed_count(0.5, stop=4):
        print(f'{current_thread().name}: {count}')


thread = Thread(target=threaded, daemon=True)
thread.start()

# Wait for thread to finish
thread.join()
