from re import *

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

print(rf"normalize('ПрИвЕт\nМИр\t') == {normalize("ПрИвЕт\nМИр\t")}")
print(rf"normalize('ёжик, Ёлка') == {normalize('ёжик, Ёлка')}")
print(rf"normalize('Hello\r\nWorld') == {normalize('Hello\r\nWorld')}")
print(rf"normalize('  двойные   пробелы  ') == {normalize('  двойные   пробелы  ')}")

def tokenize(text: str):
    return findall(r"\w+(?:-\w+)*", text)

# print(rf"tokenize('привет, мир!') == {tokenize('привет, мир!')}")
# print(rf"tokenize('hello,world!!!') == {tokenize('hello,world!!!')}")
# print(rf"tokenize('по-настоящему круто') == {tokenize('по-настоящему круто')}")
# print(rf"tokenize('2025 год') == {tokenize('2025 год')}")
# print(rf"tokenize('emoji 😀 не слово') == {tokenize('emoji 😀 не слово')}")

def count_freq(tokens: list[str]):
    freq = {}
    for w in tokens:
        freq[w] = freq.get(w,0)+1
    return freq

def top_n(freq: dict[str, int], n: int = 5):
    return sorted(freq.items(), key = lambda x: (-x[1], x[0]))[:n]

# print(rf"count_freq(['a','b','a','c','b','a']) == {count_freq(['a','b','a','c','b','a'])}")
# print(rf"top_n(count_freq(['a','b','a','c','b','a']), 2) == {top_n(count_freq(['a','b','a','c','b','a']), 2)}")

# print(rf"top_n(count_freq(['bb','aa','bb','aa','cc']), 2) == {top_n(count_freq(['bb','aa','bb','aa','cc']), 2)}")