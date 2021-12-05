import csv
from os import times

from models.Tag import Tag

def get_tags():
    tags = list()
    with open('data/tags.csv', newline='', encoding='UTF-8') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            user_id = row[0]
            movie_id = row[1]
            tag = row[2]
            timestamp = row[3]
            tag = Tag(user_id, movie_id, tag, timestamp)
            tags.append(tags)

    return tags