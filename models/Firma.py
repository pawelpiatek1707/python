class Firma:
    def __init__(self, name: str, location: str, ceo: str) -> None:
        self.__name = name
        self.__location = location
        self.__ceo = ceo

    def __str__(self) -> str:
        return f"Company {self.__name} is located in {self.__location}. CEO of {self.__name}: {self.__ceo}"

    @property
    def name(self) -> str:
        return self.__name

    @property
    def location(self) -> str:
        return self.__location

    @property
    def ceo(self) -> str:
        return self.__ceo
