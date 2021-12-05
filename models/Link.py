
class Link:
    def __init__(self, movie_id: int, imbd_id: int, tmb_id: int) -> None:
        self.__movie_id = movie_id
        self.__imbd_id = imbd_id
        self.__tmb_id = tmb_id

    @property
    def movie_id(self):
        return self.__movie_id

    @property
    def imbd_id(self):
        return self.__imbd_id

    @property
    def tmb_id(self):
        return self.__tmb_id