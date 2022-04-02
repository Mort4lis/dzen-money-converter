from typing import Iterator, Generator


class OneMoneyConverter:
    def __init__(self, csv_reader: Iterator) -> None:
        self._csv_reader = csv_reader

    def generator(self) -> Generator[tuple, None, None]:
        for row in self._csv_reader:
            if len(row) <= 2:
                break

            yield row
