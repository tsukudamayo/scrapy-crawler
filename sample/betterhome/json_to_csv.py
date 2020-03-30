import os
import json
import csv
from typing import List


_SRC_DIR = './category'


def json_to_array(filepath: str) -> List:
    with open(filepath, 'r', encoding='utf-8') as r:
        data = json.load(r)

    return [v for k, v in data.items()]


def fetch_column(filepath: str) -> List:
    with open(filepath, 'r', encoding='utf-8') as r:
        data = json.load(r)

    return [k for k, v in data.items()]


def write_csv(column: List, rows: List):
    with open('category.csv', 'w', encoding='utf-8') as w:
        csv_writer = csv.writer(w)
        csv_writer.writerow(column)
        csv_writer.writerows(rows)

    return


def main():
    file_list = os.listdir(_SRC_DIR)
    column = fetch_column(os.path.join(_SRC_DIR, file_list[0]))
    rows = [json_to_array(os.path.join(_SRC_DIR, f)) for f in file_list]
    write_csv(column, rows)


if __name__ == '__main__':
    main()

