class Student:
    def __init__(self, name: str, marks: int) -> None:
        self._name = name
        self._marks = marks

    def is_passed(self) -> bool:
        return self._marks > 50


stud1 = Student('Jan', 60)
stud2 = Student('Tomasz', 10)
print(stud1.is_passed())
print(stud2.is_passed())
