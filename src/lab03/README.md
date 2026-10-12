# Кудрявцев Евгений
# Группа БИВТ-26-6-1

# Третья лабораторная работа

## 1 Задание

1.1 normalize

Убирает из строки лишние пробелы, приводит буквы к строчным версиям и убирает невидимые управляющие символы (например \n и \t).

При casefold == True использует вместо lower casefold для занижения символов.

При yo2e == True заменяет ё/Ё на е/Е.

```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()
    if yo2e:
        text = text.replace('ё','е')
    text = text.strip()
    text = ' '.join(text.split())
    return text
```

Пример работы

![Скрин работы функции normalize](../../images/lab03/normalize.png)

1.2 tokenize

Разбивает слова по небуквенно-цифровым разделителям, за слова считает последоваетльности символов из букв, цифр, подчеркивания и дефиса внутри слова. Возвращает список.

```python
def tokenize(text: str):
    return findall(r"\w+(?:-\w+)*", text)
```

Пример работы

![Скрин работы функции tokenize](../../images/lab03/tokenize.png)

1.3 count_freq

Подсчитывает частоты строк в списке и возвращает словарь с ключами в виде уникальных значений списка и аргументами в виде количества данных элементов в словаре.

```python
def count_freq(tokens: list[str]):
    freq = {}
    for w in tokens:
        freq[w] = freq.get(w,0)+1
    return freq
```

1.4 top_n

Возвращает топ-N по убыванию частоты в словаре, при равенстве частот возвращает по алфавиту слова.

```python
def top_n(freq: dict[str, int], n: int = 5):
    return sorted(freq.items(), key = lambda x: (-x[1], x[0]))[:n]
```

Примеры работы обеих функций

![Скрин работы функций count_freq и top_n](../../images/lab03/count_freq%20+%20top_n.png)

![Скрин тай-брейка по слову при равной частоте](../../images/lab03/top_n%20равный.png)

# 2 Задание

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
    if student[2] > 5 or student[2] < 0:
        raise ValueError("GPA вне диапазона")
    
    if len(student[0].split()) == 2:
        fio = student[0].split()[0][0].upper() + student[0].split()[0][1:] + ' ' + student[0].split()[1][0].upper() + '.'
    elif len(student[0].split()) == 3:
        fio = student[0].split()[0][0].upper() + student[0].split()[0][1:] + ' ' + student[0].split()[1][0].upper() + '.' + student[0].split()[2][0].upper() + '.'
    group = student[1]
    gpa = student[2]
    return f"{fio}, гр. {group}, GPA {gpa:.2f}"
```


![Скрин выполнения третьего задания](../../images/lab02/Задание%203.2.png)
