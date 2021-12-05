from models.Kierowca import Kierowca


class Odcinek:
    def __init__(self, section_id: str, distance: float, driver: Kierowca, from_point: str, to_point: str) -> None:
        self.__section_id = section_id
        self.__distance = distance
        self.__driver = driver
        self.__from_point = from_point
        self.__to_point = to_point

    def __str__(self) -> str:
        return f"Section with id: {self.__section_id} has distance: {self.__distance}"

    @property
    def section_id(self) -> str:
        return self.__section_id

    @property
    def distance(self) -> float:
        return self.__distance

    @property
    def driver(self) -> str:
        return self.__driver

    @property
    def from_point(self) -> str:
        return self.__from_point

    @property
    def to_point(self) -> str:
        return self.__to_point
