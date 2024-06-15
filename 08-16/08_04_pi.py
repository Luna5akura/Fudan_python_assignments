import numpy as np
from multiprocessing import Pool
import time


def timeit(f, times=1):
    def wrapper(*args, time_it=True, **kwargs):
        if not time_it:
            return f(*args, **kwargs)
        start = time.time()
        ret = f(*args, **kwargs)
        for _ in range(times - 1):
            f(*args, **kwargs)
        end = time.time()
        print(f'{f.__name__} took {end - start} seconds to run {times} times')
        return ret

    return wrapper


@timeit
def PI(n):
    points = np.random.rand(n, 2)
    inside_circle = np.sum(np.sum(points ** 2, axis=1) <= 1)
    return 4 * inside_circle / n


if __name__ == '__main__':
    print(PI(1_000_000))
    print(PI(100_000_000))


def pi_wrapper(n):
    return PI(n, time_it=False)


@timeit
def main(n, processes=8):
    with Pool(processes) as pool:
        results = pool.map(pi_wrapper, [n // processes] * processes)
    return sum(results) / processes


if __name__ == '__main__':
    # print(main(100_000_000))
    pass
