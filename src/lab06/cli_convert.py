import argparse
import csv
from src.lab05.json_csv import json_to_csv, csv_to_json

def main():
    parser = argparse.ArgumentParser(description="Конвертация JSON, CSV и XLSX")
    sub = parser.add_subparsers(dest="command", required=True)

    for command, description in (("json2csv", "Преобразовать json в csv"),("csv2json", "Преобразовать csv в json"),("csv2xlsx", "Преобразовать csv в xlsx")):
        p = sub.add_parser(command,help=description,description=description)
        p.add_argument("--in",dest="input_path",required=True,help="Путь к входному файлу")
        p.add_argument("--out",dest="output_path",required=True,help="Путь к выходному файлу")

    args = parser.parse_args()

    try:
        if args.command == "json2csv":
            json_to_csv(args.input_path, args.output_path)
        elif args.command == "csv2json":
            csv_to_json(args.input_path, args.output_path)
        elif args.command == "csv2xlsx":
            from src.lab05.csv_xlsx import csv_to_xlsx
            csv_to_xlsx(args.input_path, args.output_path)

    except FileNotFoundError:
        parser.error(f"Файл не найден: {args.input_path}")

    except (ValueError, csv.Error) as error:
        parser.error(str(error))

    except UnicodeError:
        parser.error("Ошибка декодирования файла")

    except OSError as error:
        parser.error(f"Ошибка работы с файлом: {error}")

    print(f"Файл сохранён: {args.output_path}")

if __name__ == "__main__":
    main()