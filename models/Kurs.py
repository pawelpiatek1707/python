from models.Kierowca import Kierowca
from models.Pojazd import Pojazd
from models.Odcinek import Odcinek


class Kurs:
    __course_id: str
    __name: str
    __driver: Kierowca
    __distance: list
    __car: Pojazd

    def __init__(self) -> None:
        self.__course_id = ''
        self.__name = ''
        self.__driver = None
        self.__distance = [Odcinek]
        self.__car = None

    def __str__(self) -> str:
        if self.__driver != None:
            return f"Course with id {self.__course_id} whas driven by {self.__driver.name} {self.__driver.last_name}"
        else:
            return f"Course with id {self.__course_id} has no driver"

    @property
    def course_id(self) -> str:
        return self.__course_id

    @course_id.setter
    def course_id(self, value: str) -> None:
        self.__course_id = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def driver(self) -> Kierowca:
        return self.__driver

    @driver.setter
    def driver(self, value: Kierowca) -> None:
        self.__driver = value

    @property
    def distance(self) -> list:
        return self.__distance

    @distance.setter
    def distance(self, value: list) -> None:
        self.__distance = value

    @property
    def car(self) -> Pojazd:
        return self.__car

    @car.setter
    def car(self, value: Pojazd) -> None:
        self.__car = value

    def sum_distance(self) -> float:
        returned_distance: float = 0
        if self.__distance != None:
            for el in self.__distance:
                returned_distance = returned_distance + el.distance

        return format(returned_distance, ".2f")

    def get_course_car(self) -> str:
        return self.car.__brand
