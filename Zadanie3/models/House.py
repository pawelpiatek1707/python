from models.Property import Property

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