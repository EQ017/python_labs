import random
import timeit
import multiprocessing as mp
from queue import Empty
from pathlib import Path

from src.lab04.io_txt_csv import write_csv
from src.lab07.search import (linear_search,binary_search,two_sum_brute,two_sum_fast)
from src.lab07.sorting import (bubble_sort,insertion_sort,selection_sort)

def measure(fn, number=1, repeat=5):
    times = timeit.repeat(fn,number=number,repeat=repeat)
    return min(times) / number

def sort_worker(fn, data, queue):
    try:
        t = measure(lambda: fn(data),repeat=1)
        queue.put(t)
    except Exception as error:
        queue.put(str(error))
def limited_time(fn, data, limit=60, repeat=3):
    times = []
    for _ in range(repeat):
        queue = mp.Queue()
        process = mp.Process(target=sort_worker,args=(fn, data, queue))
        process.start()
        process.join(timeout=limit)
        if process.is_alive():
            process.terminate()
            process.join()
            queue.close()
            return f"> {limit} с"
        try:
            result = queue.get(timeout=5)
        except Empty:
            raise RuntimeError(f"Не удалось измерить {fn.__name__}")
        finally:
            queue.close()
        if isinstance(result, str):
            raise RuntimeError(result)
        times.append(result)
    return min(times)

def bench_sorts(n):
    data = [random.randint(-10000, 10000) for _ in range(n)]
    rows = []
    functions = (("sorted", sorted),("bubble_sort", bubble_sort),("insertion_sort", insertion_sort),("selection_sort", selection_sort))
    for name, fn in functions:
        if n == 100_000 and name != "sorted":
            t = limited_time(fn, data)
        else:
            t = measure(lambda: fn(data))
        rows.append(("sort", n, name, t))
    return rows

def bench_search():
    n = 100_000
    data = random.sample(range(1_000_000), n)
    queries = [random.randint(0, 999_999) for _ in range(10_000)]
    t_linear = measure(lambda: [linear_search(data, x) for x in queries],repeat=3)
    t_sort = measure(lambda: sorted(data))
    sorted_data = sorted(data)
    t_binary = measure(lambda: [binary_search(sorted_data, x) for x in queries])
    return [("search", n, "linear_search", t_linear),("search", n, "sort_before_binary", t_sort),("search", n, "binary_search", t_binary)]

def bench_two_sum(n):
    data = list(range(n))
    random.shuffle(data)
    target = 2 * n - 3
    rows = []
    functions = (("two_sum_brute", two_sum_brute),("two_sum_fast", two_sum_fast))
    for name, fn in functions:
        t = measure(lambda: fn(data, target))
        rows.append(("two_sum", n, name, t))
    return rows

def main():
    random.seed(42)
    rows = []
    for n in (1_000, 10_000, 100_000):
        rows.extend(bench_sorts(n))
    rows.extend(bench_search())
    for n in (1_000, 10_000):
        rows.extend(bench_two_sum(n))
    print(f"{'task':<12} {'n':<10} {'impl':<22} {'seconds':<15}")
    print("-" * 60)
    for task, n, impl, seconds in rows:
        if isinstance(seconds, float):
            seconds = f"{seconds:.6f}"
        print(f"{task:<12} {n:<10} {impl:<22} {seconds:<15}")
    path = Path("data/lab07/bench.csv")
    path.parent.mkdir(parents=True, exist_ok=True)
    write_csv(rows,path,header=("task", "n", "impl", "seconds"))
if __name__ == "__main__":
    main()
