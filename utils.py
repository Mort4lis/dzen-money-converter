import argparse
from typing import Any


def csv_file(value: Any) -> str:
    filepath = str(value)
    if not filepath.endswith(".csv"):
        raise argparse.ArgumentTypeError(f"{value} is an invalid scv file")

    return filepath
