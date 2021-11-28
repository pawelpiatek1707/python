from zad1 import Student


class Library:
    def __init__(
        self,
        city: str,
        street: str,
        zip_code: str,
        open_hours: str,
        phone: str
    ) -> None:
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return f"""Biblioteka w miescie:
                {self.city}, przy ulicy {self.zip_code}
                otwarta w godzianch {self.open_hours}"""


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


class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: str,
        birth_date: str,
        city: str,
        street: str,
        zip_code: str,
        phone: str
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return f"""Pracownik
            {self.first_name} {self.last_name} urodzony
            {self.birth_date} zatrudniony {self.hire_date}"""


class Book:
    def __init__(
        self,
        library: str,
        publication_date: str,
        author_name: str,
        author_surname: str,
        number_of_pages: int
    ) -> None:
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f"""Ksiazka z biblioteki
            {self.library}. Autor ksiazki:
            {self.author_name} {self.author_surname}"""


library1 = Library('Katowice', 'Mikołowksa', '33-123', '8-16', '653 566 762')
library1 = Library('Kraków', 'Długa', '23-423', '9-17', '453 567 654')

book1 = Book('Biblioteka Katowice', '03,10,1980', 'Jan', 'Nowak', 320)
book2 = Book('Biblioteka Kraków', '05,10,1982', 'Kamil', 'Ślimak', 320)
book3 = Book('Biblioteka Katowice', '02,10,1984', 'Stefan', 'Kowalkis', 320)
book4 = Book('Biblioteka Kraków', '07,10,1991', 'Alicja', 'Kot', 320)
book5 = Book('Biblioteka Katowice', '01,10,2012', 'Krzysztof', 'Polak', 320)

emp1 = Employee("Jan", "Nowak", "03.11.2018", "10.11.1990",
                "Katowice", "Dluga", "43-112", "123456789")
emp1 = Employee("Jan", "Kowalski", "03.09.2016", "10.11.1995",
                "Katowice", "Szeroka", "43-112", "987654321")
emp1 = Employee("Kamil", "Nowak", "03.12.2015", "10.11.1998",
                "Katowice", "Głęboka", "43-112", "654123890")

stud1 = Student("Jan", "Kowalski")
stud2 = Student("Wojciech", "Nowak")
stud3 = Student("Przemyslaw", "Polak")

order1 = Order("Jan Nowak", "Jan Kowalski", ["book1", "book2"], "03.10.2021")
order2 = Order("Kamil Slimak", "Kamil Nowak", ["book3"], "03.10.2021")

print(order1)
print(order2)
