import csv
import pandas as pd

all_movies = []
with open('movies.csv',encoding ="utf8") as f:
    file = csv.reader(f)
    data = list(file)
    all_movies = data[1:]
    headers = data[0]

headers.append('poster_link')
# print(headers)
# print(len(all_movies))
with open('final.csv', 'w') as f:
    file = csv.writer(f)
    file.writerow(headers)

all_movie_links = []
with open('posters.csv',encoding ="utf8") as f:
    file = csv.reader(f)
    data = list(file)
    all_movie_links = data[1:]

for item in all_movies:
    poster_found = any(item[8] in movie_link_items for movie_link_items in all_movie_links)
    if poster_found:
        for movie_link_item in all_movie_links:
            if item[8] == movie_link_item[0]:
                item.append(movie_link_item[1])
                if len(item) == 28:
                    with open('final.csv', 'a+', encoding ="utf8") as f:
                        file = csv.writer(f)
                        file.writerow(item)
    else:
        continue