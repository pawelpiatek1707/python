import csv

from models.Rating import Rating


def get_ratings():
    ratings = list()
    with open('data/ratings.csv', newline='', encoding='UTF-8') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            user_id = row[0]
            movie_id = row[1]
            rating = row[2]
            timestamp = row[3]
            rating = Rating(user_id, movie_id, timestamp, rating)
            ratings.append(rating)

    return ratings
