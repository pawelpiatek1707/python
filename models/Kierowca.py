class Kierowca:
    def __init__(self, driver_id: str, name: str, last_name: str) -> None:
        self.__driver_id = driver_id
        self.__name = name
        self.__last_name = last_name

    def __str__(self) -> str:
        return f"{self.__name} {self.__last_name} has id: {self.__driver_id}"

    @property
    def driver_id(self) -> str:
        return self.__driver_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def last_name(self) -> str:
        return self.__last_name
