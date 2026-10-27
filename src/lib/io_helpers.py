from re import *
import csv
from pathlib import Path
from typing import Iterable, Sequence

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

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает содержимое текстового файла и возвращает его в виде одной строки.
    По умолчанию используется кодировка utf-8. Можно читать файлы других кодировок,
    передав их в encoding.
    """
    p = Path(path)
    return p.read_text(encoding=encoding)

def ensure_parent_dir(path: str | Path) -> None:
    """Создаёт родительские папки пути, если они отсутствуют."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """Создаёт или перезаписывает CSV-файл с разделителем-запятой.
    Если указан header, он записывается в первую строку. Все строки
    должны иметь одинаковую длину, иначе возникает ValueError.
    Если rows пуст и header не задан, создаётся пустой файл.
    """
    p = Path(path)
    rows = list(rows)

    if rows:
        columns = len(rows[0])
        for r in rows:
            if len(r) != columns:
                raise ValueError("Строки имеют разное количество столбцов")

    ensure_parent_dir(p)

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=",")
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)