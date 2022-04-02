import argparse
import csv
import time
from typing import Callable

from utils import csv_file
from converters import OneMoneyConverter

types = (
    "1money",
)

parser = argparse.ArgumentParser()
parser.add_argument(
    "--input_file",
    required=True,
    type=csv_file,
    help="input CSV-file path which need to convert",
)
parser.add_argument(
    "--max-output-rows",
    type=int,
    default=1500,
    help="maximum rows in the output file",
)
parser.add_argument(
    "--input_file_type",
    choices=types,
    required=True,
    type=str,
    help="",
)


def next_output_filename_factory() -> Callable:
    seconds = int(time.time())
    output_files_counter = 0

    def inner() -> str:
        nonlocal output_files_counter

        output_files_counter += 1
        return f"output-{seconds}_{output_files_counter}.csv"

    return inner


def new_csv_writer(file):
    writer = csv.writer(file)

    writer.writerow([
        "Дата", "Категория",
        "Плательщик", "Счет",
        "Сумма-расход", "Счет-получатель",
        "Сумма-доход", "Комментарий"
    ])

    return writer


def main() -> None:
    args = parser.parse_args()
    next_output_filename = next_output_filename_factory()

    rows_counter = 1

    with open(args.input_file, mode="r") as infile:
        reader = csv.reader(infile)
        headers = next(reader)

        print("Headers", headers)

        output_file = open(next_output_filename(), mode="w")
        writer = new_csv_writer(output_file)

        converter = OneMoneyConverter(reader)

        for row in converter.generator():
            writer.writerow(row.to_tuple())
            rows_counter += 1

            if rows_counter == args.max_output_rows:
                rows_counter = 1

                output_file.close()
                output_file = open(next_output_filename(), mode="w")
                writer = new_csv_writer(output_file)

        output_file.close()


if __name__ == "__main__":
    main()
