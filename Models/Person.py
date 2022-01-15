class Person:
    def __init__(self, id: str, name: str, last_name: str) -> None:
        self.__id = id
        self.__name = name
        self.__last_name = last_name

    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def last_name(self) -> str:
        return self.__last_name

    def __str__(self) -> str:
        return f"{self.__name} {self.__last_name}"
