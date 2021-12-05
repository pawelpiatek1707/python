from models.Property import Property

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