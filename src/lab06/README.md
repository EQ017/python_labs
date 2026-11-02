# Кудрявцев Евгений
# Группа БИВТ-26-6-1

# Шестая лабораторная работа

# Задание A

В файле `src/lab06/cli_text.py` имеются 2 подкоманды: `cat` и `stats`

`cat --input <путь> [-n]` Печатает файл по строкам, `-n` нумерует строки, начиная с 1

Пример команды в консоли
```
python3 -m src.lab06.cli_text cat --input data/samples/people.csv -n
```

![Скрин](../../images/lab06/img1.png)

`stats --input <путь> [--top n]` Пишет число слов и число уникальных слов и n-число самых частых слов с количеством. По умолчанию n = 5

Пример команды в консоли
```
python3 -m src.lab06.cli_text stats --input data/samples/people.csv --top 5
```

![Скрин](../../images/lab06/img2.png)

# Задание B

В файле `src/lab06/cli_text.py` имеются 3 подкоманды: `json2csv`, `csv2json` и `csv2xlsx`, которые вызывают функции из 5 лабораторной работы

`json2csv` преобразует json-файл в csv-файл

Пример команды в консоли
```
python3 -m src.lab06.cli_convert json2csv --in data/samples/people.json --out data/out/people.csv
```

`csv2json` преобразует csv-файл в json-файл

Пример команды в консоли
```
python3 -m src.lab06.cli_convert csv2json --in data/samples/people.csv --out data/out/people.json
```

`csv2xlsx` преобразует csv-файл в xlsx-файл

Пример команды в консоли
```
python3 -m src.lab06.cli_convert csv2xlsx --in data/samples/people.csv --out data/out/people.xlsx
```

![Скрин](../../images/lab06/img3.png)

*help справки*

```
python3 -m src.lab06.cli_text --help
python3 -m src.lab06.cli_text stats --help
python3 -m src.lab06.cli_convert --help
python3 -m src.lab06.cli_convert json2csv --help
```

![Скрин](../../images/lab06/img4.png)

![Скрин](../../images/lab06/img5.png)

![Скрин](../../images/lab06/img6.png)

![Скрин](../../images/lab06/img7.png)

*Возможные ошибки*

1. Отсутсвие входного файла
2. Неверное расширение файла
3. Кодировка файла не UTF-8
4. stats --top 0; --top должен быть положительным
5. Не указана подкоманда

![Скрин](../../images/lab06/шьп8.png)
