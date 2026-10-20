import sys
import argparse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lib.text import normalize, tokenize, count_freq, top_n
from lab04.io_txt_csv import read_text, write_csv


parser = argparse.ArgumentParser()

parser.add_argument("--in", dest="input_path", default="data/lab04/input.txt")

parser.add_argument("--out", dest="output_path", default="data/lab04/report.csv")

parser.add_argument("--encoding", default="utf-8")

args = parser.parse_args()

text = read_text(args.input_path, encoding=args.encoding)

freq = count_freq(tokenize(normalize(text)))

rows = sorted(freq.items(), key=lambda p: (-p[1], p[0]))

write_csv(rows, args.output_path, header=("word","count"))

print(f"Всего слов: {sum(freq.values())}")
print(f"Уникальных слов: {len(freq)}")
print("Топ-5:")
for w, c in top_n(freq, 5):
    print(f"{w}:{c}")