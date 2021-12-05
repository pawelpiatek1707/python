from models.Firma import Firma


class Firma_Spozywcza(Firma):
    def __init__(self, name: str, location: str, ceo: str, founding_date: str, numer_of_shops: int) -> None:
        super().__init__(name, location, ceo)
        self.__founding_date = founding_date
        self.__number_of_shops = numer_of_shops

    def __str__(self) -> str:
        return f"Food company {self.__name} has {self.numer_of_shops} shops"

    @property
    def founding_date(self) -> str:
        return self.__founding_date

    @property
    def numer_of_shops(self) -> int:
        return self.__number_of_shops
