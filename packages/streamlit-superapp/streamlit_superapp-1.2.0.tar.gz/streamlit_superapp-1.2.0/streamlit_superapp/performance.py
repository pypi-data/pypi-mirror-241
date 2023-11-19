import functools
import time


def gather(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        print(f"{func.__name__}: {round(((time.time() - start_time) * 1000), 2) } ms")
        return ret

    return wrapper
