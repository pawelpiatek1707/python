from controllers.get_movies import get_movies

movies = get_movies()

for movie in movies:
    print(movie)
