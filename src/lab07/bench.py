import random
import timeit
from pathlib import Path

from src.lab04.io_txt_csv import write_csv
from src.lab07.search import (linear_search,binary_search,two_sum_brute,two_sum_fast)
from src.lab07.sorting import (bubble_sort,insertion_sort,selection_sort)

def measure(fn, number=1, repeat=5):
    times = timeit.repeat(fn,number=number,repeat=repeat)
    return min(times) / number

def bench_sorts(n, previous_times):
    data = [random.randint(-10000, 10000) for _ in range(n)]
    rows = []
    functions = (("sorted", sorted),("bubble_sort", bubble_sort),("insertion_sort", insertion_sort),("selection_sort", selection_sort))
    for name, fn in functions:
        if n == 100_000 and name != "sorted":
            estimated = previous_times[name] * (n / 10_000) ** 2
            if estimated > 60:
                t = "> 60 с (оценка)"
            else:
                t = measure(lambda: fn(data),repeat=3)
        else:
            t = measure(lambda: fn(data))
        if n == 10_000:
            previous_times[name] = t
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
    previous_times = {}
    for n in (1_000, 10_000, 100_000):
        rows.extend(bench_sorts(n, previous_times))
    rows.extend(bench_search())
    for n in (1_000, 10_000):
        rows.extend(bench_two_sum(n))
    print(f"{'task':<12} {'n':<10} {'impl':<22} {'seconds':<20}")
    print("-" * 65)
    for task, n, impl, seconds in rows:
        if isinstance(seconds, float):
            seconds = f"{seconds:.6f}"
        print(f"{task:<12} {n:<10} {impl:<22} {seconds:<20}")
    path = Path("data/lab07/bench.csv")
    path.parent.mkdir(parents=True, exist_ok=True)
    write_csv(rows,path,header=("task", "n", "impl", "seconds"))

if __name__ == "__main__":
    main()
