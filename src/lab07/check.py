import random
from src.lab07.search import (linear_search,binary_search,two_sum_brute,two_sum_fast)
from src.lab07.sorting import (bubble_sort,insertion_sort,selection_sort)

def check_sorting(fn, trials=100):
    cases = [[], [5], [2, 2, 1], [-3, 0, -3]]
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        cases.append(nums)
    for nums in cases:
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), (f"{fn.__name__} ошиблась на {nums}: {result}")
        assert nums == original, (f"{fn.__name__} изменила исходный список: {nums}")
    return len(cases)


def check_search():
    count = 0
    for _ in range(100):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        for x in (-101, 0, 101):
            try:
                expected = nums.index(x)
            except ValueError:
                expected = -1

            assert linear_search(nums, x) == expected, (f"linear_search ошиблась: nums={nums}, x={x}")
            count += 1
        sorted_nums = sorted(nums)
        queries = [-101, 101]
        if sorted_nums:
            queries += [sorted_nums[0], sorted_nums[-1]]
        for x in queries:
            result = binary_search(sorted_nums, x)
            if x in sorted_nums:
                assert 0 <= result < len(sorted_nums) and sorted_nums[result] == x, (f"binary_search ошиблась: nums={sorted_nums}, x={x}")
            else:
                assert result == -1, (f"binary_search ошиблась: nums={sorted_nums}, x={x}")
            count += 1
    return count


def check_two_sum(trials=100):
    cases = [([], 5),([1], 2),([2, 7, 11, 15], 9),([3, 3], 6),([1, 2], 10),([1, 2, 3, 4], 5)]
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        target = random.randint(-200, 200)
        cases.append((nums, target))
    for nums, target in cases:
        brute = two_sum_brute(nums, target)
        fast = two_sum_fast(nums, target)
        assert (brute is None) == (fast is None), (f"Two Sum: расхождение на {nums}, target={target}")
        for result in (brute, fast):
            if result is not None:
                i, j = result
                assert 0 <= i < j < len(nums), (f"Неверные индексы: {result}, nums={nums}")
                assert nums[i] + nums[j] == target, (f"Неверная сумма: {result}, nums={nums}")

    return len(cases)


if __name__ == "__main__":
    random.seed(42)
    total = 0
    for fn in (bubble_sort, insertion_sort, selection_sort):
        total += check_sorting(fn)
    total += check_search()
    total += check_two_sum()
    print(f"OK: {total} проверок")
