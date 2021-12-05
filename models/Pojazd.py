class Pojazd:
    def __init__(self, brand: str, color: str, wheels: int, load: int, top_speed: int) -> None:
        self.__brand = brand
        self.__color = color
        self.__wheels = wheels
        self.__load = load
        self.__top_speed = top_speed

    def __str__(self) -> str:
        return f"Car: {self.__brand} with {self.__wheels} wheels is {self.__color} and can take {self.__load} load"

    @property
    def brand(self) -> str:
        return self.__brand

    @property
    def color(self) -> str:
        return self.__color

    @property
    def wheels(self) -> int:
        return self.__wheels

    @property
    def load(self) -> int:
        return self.__load

    @property
    def top_speed(self) -> int:
        return self.__top_speed
