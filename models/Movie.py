class Movie:
    def __init__(self, movie_id: int, title: str, genres: list) -> None:
        self.__movie_id = movie_id
        self.__title = title
        self.__genres = genres

    @property
    def movie_id(self):
        return self.__movie_id

    @property
    def title(self):
        return self.__title

    @property
    def genres(self):
        return self.__genres

    def __str__(self) -> str:
        return f"movie with id: {self.__movie_id} and title: {self.__title}"
