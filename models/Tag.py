class Tag:
    def __init__(self, user_id: int, movie_id: int, tag: str, timestamp: int) -> None:
        self.__user_id = user_id
        self.__movie_id = movie_id
        self.__tag = tag
        self.__timestamp = timestamp

    @property
    def movie_id(self):
        return self.__movie_id

    @property
    def user_id(self):
        return self.__user_id

    @property
    def tag(self):
        return self.__tag

    @property
    def timestamp(self):
        return self.__timestamp
