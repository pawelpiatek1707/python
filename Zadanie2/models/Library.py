
class Library:
    def __init__(
        self,
        city: str,
        street: str,
        zip_code: str,
        open_hours: str,
        phone: str
    ) -> None:
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return f"""Biblioteka w miescie:
                {self.city}, przy ulicy {self.zip_code}
                otwarta w godzianch {self.open_hours}"""