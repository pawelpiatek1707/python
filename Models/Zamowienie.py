from Models.Pacjent import Pacjent
from Models.Dieta import Dieta


class Zamowienie:
    __order_id: str
    __date: str
    __client: Pacjent
    __diets: list

    def __init__(self) -> None:
        self.__order_id = ''
        self.__date = ''
        self.__client = None
        self.__diets = [Dieta]

    def __str__(self) -> str:
        if self.__client != None:
            return f"{self.__client} bought diet at {self.__date}"
        else:
            return f"Order has no client"

    def get_price(self) -> float:
        price = 0
        for diet in self.__diets:
            price = price + diet.diet_price

        return format(price, ".2f")

    def get_calories(self) -> float:
        calories = 0
        for diet in self.__diets:
            calories = calories + diet.calories

        return format(calories, ".2f")

    @property
    def order_id(self) -> str:
        return self.__order_id

    @order_id.setter
    def order_id(self, value: str) -> None:
        self.__order_id = value

    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, value: str) -> None:
        self.__date = value

    @property
    def client(self) -> Pacjent:
        return self.__client

    @client.setter
    def client(self, value: Pacjent) -> None:
        self.__client = value

    @property
    def diets(self) -> Dieta:
        return self.__diets

    @diets.setter
    def diets(self, value: Dieta) -> None:
        self.__diets = value
