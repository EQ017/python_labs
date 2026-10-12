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

def tokenize(text: str):
    return findall(r"\w+(?:-\w+)*", text)

def count_freq(tokens: list[str]):
    freq = {}
    for w in tokens:
        freq[w] = freq.get(w,0)+1
    return freq

def top_n(freq: dict[str, int], n: int = 5):
    return sorted(freq.items(), key = lambda x: (-x[1], x[0]))[:n]
