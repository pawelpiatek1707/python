import csv

from models.Link import Link


def get_links():
    links = list()
    with open('data/links.csv', newline='', encoding='UTF-8') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            movie_id = row[0]
            imbd_id = row[1]
            tmb_id = row[2]
            link = Link(movie_id, imbd_id, tmb_id)
            links.append(link)

    return links
