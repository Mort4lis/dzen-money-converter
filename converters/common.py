from copy import deepcopy


class OutputRow:
    __slots__ = (
        "date", "category", "payer",
        "account", "total_sum_expense", "account_to",
        "total_sum_income", "comment"
    )

    def __init__(self):
        self.date = ""
        self.category = ""
        self.payer = ""
        self.account = ""
        self.total_sum_expense = ""
        self.account_to = ""
        self.total_sum_income = ""
        self.comment = ""

    def to_tuple(self) -> tuple:
        return (
            self.date, self.category, self.payer,
            self.account, self.total_sum_expense, self.account_to,
            self.total_sum_income, self.comment
        )

    def copy(self) -> "OutputRow":
        return deepcopy(self)
