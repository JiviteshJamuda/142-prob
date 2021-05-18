import csv 
import pandas as pd

all_movies = []
with open('final.csv', encoding ="utf8") as f:
    file = csv.reader(f)
    data = list(file)
    all_movies = data[1:]

liked_movies = []
disliked_movies = []
movies_not_watched = []