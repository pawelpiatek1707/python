class Rating:
    def __init__(self, user_id: int, movie_id: int, rating: int, timestamp: int) -> None:
        self.__user_id = user_id
        self.__movie_id = movie_id
        self.__rating = rating
        self.__timestamp = timestamp
# userId,movieId,rating,timestamp

    @property
    def movie_id(self):
        return self.__movie_id

    @property
    def user_id(self):
        return self.__user_id

    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def rating(self):
        return self.__rating