
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


kierowca1 = Kierowca('3623ygssw', 'Jan', 'Kowalski')

odcinek1 = Odcinek('3322fjfdi112', 231.5, kierowca1, 'Katowice', 'Krakow')
odcinek2 = Odcinek('543dfwfvef', 315.654, kierowca1, 'Krakow', 'Warszawa')

pojazd1 = Pojazd('Renault', 'czerwony', 8, 20, 110)

kurs = Kurs()
kurs.course_id = 'ovbruvbuon2313dxc'
kurs.name = 'Kurs1'
kurs.driver = kierowca1
kurs.distance = [odcinek1, odcinek2]
kurs.car = pojazd1

print(kurs)
print(kurs.sum_distance())
print(kurs.car)





