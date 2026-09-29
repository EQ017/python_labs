def min_max(nums):
    if len(nums) == 0:
        raise ValueError("Ошибка: список пуст")
    mn = mx = nums[0]
    for n in nums:
        if n < mn:
            mn = n
        if n > mx:
            mx = n
    return (mn,mx)

def unique_sorted(nums):
    n = []
    for x in nums:
        if x in n:
            continue
        p = 0
        while p < len(n) and n[p] < x:
            p += 1
        n.insert(p,x)
    return n

def flatten(nums):
    n = []
    for x in nums:
        if type(x) != list and type(x) != tuple:
            raise TypeError("Ошибка: элемент не является ни списком, ни кортежем")
        for y in x:
            n.append(y)
    return n

# print("min_max")
# print(f"{[3,-1,5,5,0]} -> {min_max([3,-1,5,5,0])}")
# print(f"{[42]} -> {min_max([42])}")
# print(f"{[-5,-2,-9]} -> {min_max([-5,-2,-9])}")
# print(f"{[1.5,2,2.0,-3.1]} -> {min_max([1.5,2,2.0,-3.1])}")
# print(f"{[]} -> {min_max([])}")
# print("Hi")

# print("unique_sorted")
# print(f"{[3,1,2,1,3]} -> {unique_sorted([3,1,2,1,3])}")
# print(f"{[-1,-1,0,2,2]} -> {unique_sorted([-1,-1,0,2,2])}")
# print(f"{[1.0,1,2.5,2.5,0]} -> {unique_sorted([1.0,1,2.5,2.5,0])}")
# print(f"{[]} -> {unique_sorted([])}")

print("flatten")
print(f"{[[1,2],[3,4]]} -> {flatten([[1,2],[3,4]])}")
print(f"{[[1,2],(3,4,5)]} -> {flatten([[1,2],(3,4,5)])}")
print(f"{[[1],[],[2,3]]} -> {flatten([[1],[],[2,3]])}")
print(f"{[[1,2],"ab"]} -> {flatten([[1,2],"ab"])}")