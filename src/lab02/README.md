# Кудрявцев Евгений
# Группа БИВТ-26-6-1

# Лабараторная работа номер 2

## 1 Задание

1.1 min_max

Возвращает минимальное и максимальное число из списка

```python
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
```

![Скрин выполнения первого задания min_max](../../images/lab02/Задание%201.2.png)

1.2 unique_sorted

Сортирует список, убирая повторы

```python
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
```

![Скрин выполнения первого задания unique_sorted](../../images/lab02/Задание%201.2(1).png)

1.3 flatten

Объединяет кортежи и списки в единый список

```python
def flatten(nums):
    n = []
    for x in nums:
        if type(x) != list and type(x) != tuple:
            raise TypeError("Ошибка: элемент не является ни списком, ни кортежем")
        for y in x:
            n.append(y)
    return n
```

![Скрин выполнения первого задания flatten](../../images/lab02/Задание%201.2(2).png)

## 2 Задание

2.1 transpose

Транспонирует матрицу(меняет строки и столбы местами)

```python
def transpose(mat):
    n = []
    if len(mat) > 0:
        ln = len(mat[0])
        for x in mat:
            if len(x) != ln:
                raise ValueError("Ошибка: рваная матрица")
        for x in range(ln):
            new_mat = []
            for y in mat:
                new_mat.append(y[x])
            n.append(new_mat)
    return n
```

![Скрин выполнения второго задания transpose](../../images/lab02/Задание%202.2.png)

2.2 row_sums

Считает суммы элементов в строках матрицы

```python
def row_sums(mat):
    n = []
    ln = len(mat[0])
    for x in mat:
        if len(x) != ln:
            raise ValueError("Ошибка: рваная матрица")
        n.append(sum(x))
    return n
```

![Скрин выполнения второго задания row_sums](../../images/lab02/Задание%202.2(1).png)

2.3 col_sums

Считает суммы элементов в столбах матрицы

```python
def row_sums(mat):
    n = []
    mat = transpose(mat)
    ln = len(mat[0])
    for x in mat:
        if len(x) != ln:
            raise ValueError("Ошибка: рваная матрица")
        n.append(sum(x))
    return n
```

![Скрин выполнения второго задания col_sums](../../images/lab02/Задание%202.2(2).png)

# 3 Задание

Получает кортеж с ФИО, группой и GPA и формирует строку с фамилией, инициалами, группой и средним баллом

Также выполняется проверка входных данных

```python
def format_record(student):
    if type(student) != tuple:
        raise TypeError("Входные данные должны являться кортежем")
    if len(student) != 3:
        raise ValueError("Неверное количество элементов")
    if type(student[0]) != str or len(student[0]) <= 0:
        raise TypeError("Неверное ФИО")
    if type(student[1]) != str:
        raise TypeError("Неверная группа")
    if type(student[2]) != float:
        raise TypeError("Неверная GPA")
    
    if len(student[0].split()) == 2:
        fio = student[0].split()[0][0].upper() + student[0].split()[0][1:] + ' ' + student[0].split()[1][0].upper() + '.'
    elif len(student[0].split()) == 3:
        fio = student[0].split()[0][0].upper() + student[0].split()[0][1:] + ' ' + student[0].split()[1][0].upper() + '.' + student[0].split()[2][0].upper() + '.'
    group = student[1]
    gpa = student[2]
    return f"{fio}, гр. {group}, GPA {gpa:.2f}"
```


![Скрин выполнения третьего задания](../../images/lab02/Задание%203.2.png)
