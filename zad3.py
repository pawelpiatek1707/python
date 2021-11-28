class Property:
    def __init__(
        self,
        area: int,
        rooms: int,
        price: int,
        address: str
    ) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(
        self,
        area: int,
        rooms: int,
        price: int,
        address: str,
        plot: int
    ) -> None:
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self) -> str:
        return f"{self.area} house with {self.rooms} rooms, for {self.price}$"


class Flat(Property):
    def __init__(
        self,
        area: int,
        rooms: int,
        price: int,
        address: str,
        floor: int
    ) -> None:
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self) -> str:
        return f"""{self.area} flat with {self.rooms}
            rooms, located in {self.address}"""


house = House(120, 6, 300000, 'Katowice', 500)
flat = Flat(56, 3, 200000, 'Katowice', 4)

print(house)
print(flat)
