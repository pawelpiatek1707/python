
class Order:
    def __init__(
        self,
        employee: str,
        student: str,
        books: list,
        order_date: str
    ) -> None:
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        return f"""Zamowienie zamowione dnia:
            {self.order_date}, przez {self.student},
            zrealizowane przez {self.employee}"""