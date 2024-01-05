import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEST_DATA_DIR = BASE_DIR.joinpath('test_data')


def get_CSV_data_as_dict(filename):
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, 'r') as file:
        csv_file = csv.reader(file)
        headers = next(csv_file)
        dict_list = [dict(zip(headers, row)) for row in csv_file]

    return dict_list


def get_data_as_list(filename):
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, 'r') as file:
        csv_file = csv.reader(file)
        next(csv_file)
        lines = list(csv_file)

    return lines
