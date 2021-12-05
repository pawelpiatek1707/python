from models.Firma import Firma


class Firma_Transportowa(Firma):
    def __init__(self, name: str, location: str, ceo: str, number_of_cars: int, employers: int) -> None:
        super().__init__(name, location, ceo)
        self.__number_of_cars = number_of_cars
        self.__employers = employers

    def __str__(self) -> str:
        return f"transportation compay {self.__name} has {self.__number_of_cars} cars and {self.__employers} employers"

    @property
    def number_of_cars(self) -> int:
        return self.__number_of_cars

    @property
    def employers(self) -> int:
        return self.__employers
