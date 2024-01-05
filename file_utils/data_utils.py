import csv
from pathlib import Path

#print("BASE_DIR:", Path(__file__).resolve().parent.parent)

BASE_DIR = Path(__file__).resolve().parent.parent
TEST_DATA_DIR = BASE_DIR.joinpath('test_data')


def get_CSV_data_as_dict(filename):
    filepath = TEST_DATA_DIR.joinpath(filename)

    try:
        with open(filepath, 'r') as file:
            csv_file = csv.reader(file)
            headers = next(csv_file)
            dict_list = [dict(zip(headers, row)) for row in csv_file]
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {filepath}") from e
    except csv.Error as e:
        raise ValueError(f"Error reading CSV file {filepath}: {e}") from e

    return dict_list
