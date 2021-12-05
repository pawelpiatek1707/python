class Student:
    def __init__(self, name: str, marks: int) -> None:
        self._name = name
        self._marks = marks

    def is_passed(self) -> bool:
        return self._marks > 50

