from typing import Iterator, Generator
from .common import OutputRow

INCOME_OP_TYPE = "Доход"
EXPENSE_OP_TYPE = "Расход"
TRANSFER_OP_TYPE = "Перевод"

INCOME_CATEGORY_PATH = "Доходы / {0}"


class OneMoneyConverter:
    def __init__(self, csv_reader: Iterator) -> None:
        self._csv_reader = csv_reader

    def generator(self) -> Generator[OutputRow, None, None]:
        for source_row in self._csv_reader:
            if len(source_row) < 10:
                break

            date, operation_type, from_account, to, total_sum, currency, _, _, _, notes, *_ = source_row

            output_row = OutputRow()

            output_row.date = date
            output_row.comment = notes

            if operation_type == EXPENSE_OP_TYPE:
                output_row.category = to
                output_row.account = from_account
                output_row.total_sum_expense = total_sum
            elif operation_type == INCOME_OP_TYPE:
                output_row.category = INCOME_CATEGORY_PATH.format(to)
                output_row.account_to = from_account
                output_row.total_sum_income = total_sum
            elif operation_type == TRANSFER_OP_TYPE:
                output_row.category = TRANSFER_OP_TYPE

                copied = output_row.copy()

                copied.account_to = to
                copied.total_sum_income = total_sum

                yield copied

                output_row.account = from_account
                output_row.total_sum_expense = total_sum
            else:
                continue

            yield output_row
