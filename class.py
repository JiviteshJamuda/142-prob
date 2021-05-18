from flask import Flask, jsonify, request
import csv
import pandas as pd
from demographic_filtering import output
from content_filtering import get_recomendation
from storage import all_movies, liked_movies, disliked_movies, movies_not_watched

app = Flask(__name__)
@app.route('/get-movie')

def get_movie():
    movie_data = {
        'title'        : all_movies[0][19],
        'poster_link'  : all_movies[0][27],
        'release_date' : all_movies[0][13] or 'na',
        'duration'     : all_movies[0][15],
        'rating'       : all_movies[0][20],
        'overview'     : all_movies[0][9],
    }
    return jsonify({
        'data' : movie_data,
        'status' : 'success',
    }),200

@app.route('/liked-movie', methods = ['POST'])

def liked_movie():
    movie = all_movies[0]
    # all_movies = all_movies[1:]
    liked_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        'status' : 'success',
    }),201

@app.route('/disliked-movie', methods = ['POST'])

def disliked_movie():
    movie = all_movies[0]
    # all_movies = all_movies[1:]
    disliked_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        'status' : 'success',
    }),202

@app.route('/movies-not-watched', methods = ['POST'])

def movie_not_watched():
    movie = all_movies[0]
    # all_movies = all_movies[1:]
    movies_not_watched.append(movie)
    all_movies.pop(0)
    return jsonify({
        'status' : 'success',
    }),203

@app.route('/popular-movies')

def popular_movie():
    movie_data = []
    for movie in output:
        d = {
            'title'        : movie[0],
            'poster_link'  : movie[1],
            'release_date' : movie[2] or 'na',
            'duration'     : movie[3],
            'rating'       : movie[4],
            'overview'     : movie[5],
        }
        movie_data.append(d)
    return jsonify({
        'data' : movie_data,
        'status' : 'success'
    }),204

@app.route('/recommended-movies')

def recommended_movies():
    all_recommended = []
    for liked_movie in liked_movies:
        output = get_recomendation(liked_movie[19])
        
        for data in output:
            all_recommended.append(data)
    
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended, _ in itertools.groupby(all_recommended))
    movie_data = []
    for movie in all_recommended:
        d = {
            'title'        : movie[0],
            'poster_link'  : movie[1],
            'release_date' : movie[2] or 'na',
            'duration'     : movie[3],
            'rating'       : movie[4],
            'overview'     : movie[5],
        }
        movie_data.append(d)
    return jsonify({
        'data' : movie_data,
        'status' : 'success'
    }),205

if __name__ == '__main__':
    app.run()