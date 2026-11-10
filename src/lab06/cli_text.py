import argparse

from src.lib.io_helpers import (read_text,normalize,tokenize,count_freq,top_n)

def main():
    parser = argparse.ArgumentParser(description="Работа с текстовыми файлами")
    sub = parser.add_subparsers(dest="command",required=True)

    cat_parser = sub.add_parser("cat",help="Вывести содержимое файла")
    cat_parser.add_argument("--input",required=True,help="Путь к входному файлу UTF-8")
    cat_parser.add_argument("-n",action="store_true",help="Нумеровать строки")

    stats_parser = sub.add_parser("stats",help="Посчитать частоты слов")
    stats_parser.add_argument("--input",required=True,help="Путь к входному файлу UTF-8")
    stats_parser.add_argument("--top",type=int,default=5,help="Количество слов в топе (по умолчанию 5)")

    args = parser.parse_args()

    if args.command == "stats" and args.top <= 0:
        stats_parser.error("--top должен быть положительным числом")

    try:
        if args.command == "cat":
            with open(args.input, encoding="utf-8") as file:
                for number, line in enumerate(file, start=1):
                    if args.n:
                        print(f"{number}: {line}", end="")
                    else:
                        print(line, end="")

        elif args.command == "stats":
            text = read_text(args.input)
            words = tokenize(normalize(text))
            freq = count_freq(words)

            print(f"Всего слов: {len(words)}")
            print(f"Уникальных слов: {len(freq)}")
            print(f"Топ-{args.top}:")

            for word, count in top_n(freq, args.top):
                print(f"{word}: {count}")

    except FileNotFoundError:
        parser.error(f"Файл не найден: {args.input}")

    except UnicodeDecodeError:
        parser.error("Не удалось прочитать файл в кодировке UTF-8")

    except OSError as error:
        parser.error(f"Ошибка работы с файлом: {error}")

if __name__ == "__main__":
    main()