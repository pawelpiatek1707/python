from Zadanie1.models.Student import Student
from Zadanie2.models.Library import Library
from Zadanie2.models.Book import Book
from Zadanie2.models.Employee import Employee
from Zadanie2.models.Order import Order
from Zadanie3.models.House import House
from Zadanie3.models.Flat import Flat


# Zadanie 1
stud1 = Student('Jan', 60)
stud2 = Student('Tomasz', 10)
# print(stud1.is_passed())
# print(stud2.is_passed())

# Zadanie 2
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

# Zadanie 3

house = House(120, 6, 300000, 'Katowice', 500)
flat = Flat(56, 3, 200000, 'Katowice', 4)

print(house)
print(flat)
