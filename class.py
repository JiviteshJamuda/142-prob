from flask import Flask, jsonify, request
import csv
import pandas as pd

all_movies = []
data = []
with open('movies.csv',encoding ="utf8") as f:
    file = csv.reader(f)
    data = list(file)
    all_movies = data[1:]

liked_movies = []
disliked_movies = []
movies_not_watched = []

app = Flask(__name__)
@app.route('/get-movie')

def get_movie():
    return jsonify({
        'data' : all_movies[0],
        'status' : 'success',
    })

@app.route('/liked-movie', methods = ['POST'])

def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        'status' : 'success',
    })

@app.route('/disliked-movie', methods = ['POST'])

def disliked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    disliked_movies.append(movie)
    return jsonify({
        'status' : 'success',
    })

@app.route('/movies-not-watched', methods = ['POST'])

def movie_not_watched():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    movies_not_watched.append(movie)
    return jsonify({
        'status' : 'success',
    })

app.run()