import csv
from pathlib import Path
from typing import Iterable, Sequence

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

# print("utf-8:")
# Path("data/lab04/input.txt").write_text("Привет, мир! Привет!!!",encoding="utf-8")
# print(repr(read_text("data/lab04/input.txt")))

# print("\nПустой файл:")
# Path("data/lab04/input.txt").write_text('',encoding="utf-8")
# print(repr(read_text("data/lab04/input.txt")))

# print("\ncp1251:")
# Path("data/lab04/input.txt").write_text("Привет", encoding="cp1251")
# print(repr(read_text("data/lab04/input.txt", encoding="cp1251")))

# print("\nОтсутсвие файла:")
# try:
#     read_text("data/lab04/67.txt")
# except FileNotFoundError:
#     print("FileNotFoundError: файл с данным названием отстутвует")

# print("\nНеверная кодировка:")
# try:
#     read_text("data/lab04/input.txt", encoding="utf-8")
# except UnicodeDecodeError:
#     print("UnicodeDecodeError: неверная кодировка файла")

# Path("data/lab04/input.txt").write_text("Привет, мир! Привет!!!",encoding="utf-8")

# write_csv([("test", 3)], "data/lab04/check.csv", header=("word", "count"))
# print("\nCSV с заголовком:")
# print(read_text("data/lab04/check.csv",encoding="utf-8"), end="")

# write_csv([], "data/lab04/check.csv", header=("word", "count"))
# print("\nПустые строки с заголовком:")
# print(read_text("data/lab04/check.csv",encoding="utf-8"), end="")

# write_csv([], "data/lab04/check.csv")
# print("\nПустые строки без заголовка:")
# print(repr(read_text("data/lab04/check.csv",encoding="utf-8")))

# print("\nCтроки разной длины:")
# try:
#     write_csv([("Me", 1), ("You",)], "data/lab04/check.csv")
# except ValueError:
#     print("ValueError: строки разной длины")