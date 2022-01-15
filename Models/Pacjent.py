from Models.Person import Person


class Pacjent(Person):
    def __init__(self, id: str, name: str, last_name: str, disease: str) -> None:
        super().__init__(id, name, last_name)
        self.__disease = disease

    @property
    def disease(self) -> str:
        return self.__disease

    def __str__(self) -> str:
        return f"{self._name} {self._last_name} has {self.__disease}"
