from Models.Dietetyk import Dietetyk


class Dieta:
    def __init__(self, id: str, name: str, price: float, author: Dietetyk, calories: float) -> None:
        self.__diet_id = id
        self.__diet_name = name
        self.__diet_price = price
        self.__diet_author = author
        self.__calories = calories

    @property
    def diet_id(self) -> str:
        return self.__diet_id

    @property
    def diet_name(self) -> str:
        return self.__diet_name

    @property
    def diet_price(self) -> float:
        return self.__diet_price

    @property
    def diet_author(self) -> str:
        return self.__diet_author

    @property
    def calories(self) -> float:
        return self.__calories

    def __str__(self) -> str:
        return f"""Dieta {self.__diet_name}
                kosztuje {self.__diet_price}.
                Autorem diety jest {self.__diet_author}.
                Dieta ma {self.__calories} kalorii"""
