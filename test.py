from controllers.get_movies import get_movies
from controllers.get_links import get_links

movies = get_movies()
# links = get_links()

# for link in links:
#     print(link)

for movie in movies:
    print(movie)
