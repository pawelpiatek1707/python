import csv

from models.Movie import Movie

def get_movies():
    movies = list()
    with open('data/movies.csv', newline='', encoding='UTF-8') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            movie_id = row[0]
            movie_title = row[1]
            movie_genres = row[2].split("|")
            movie = Movie(movie_id, movie_title, movie_genres)
            movies.append(movie)

    return movies
