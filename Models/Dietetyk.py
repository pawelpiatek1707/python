from Models.Person import Person


class Dietetyk(Person):
    def __init__(self, id: str, name: str, last_name: str, specialization: str) -> None:
        super().__init__(id, name, last_name)
        self.__specialization = specialization

    @property
    def specialization(self) -> str:
        return self.__specialization

    def __str__(self) -> str:
        return f"{self._name} {self._last_name} has {self.__specialization} specialization"
