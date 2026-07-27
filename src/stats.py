from src.database import get_session, Movie
import pandas as pd
from pandas import DataFrame

# Takes Movie rows and puts them into a dataframe
def get_movies_dataframe():
    session = get_session()
    movies = session.query(Movie).all()

    # List comprehension that converts Movie objects into a dictionary
    movie_data = [
        {
            'title': movie.title,
            'genres': movie.genres,
            'director': movie.director,
            'release_year': movie.release_year,
            'my_rating': movie.my_rating,
            'vote_average': movie.vote_average,
            'date_watched': movie.date_watched
        }
        for movie in movies
    ]

    session.close()
    df = pd.DataFrame(movie_data)
    return df

# Handling genre normalisation issue
def genre_breakdown():
    data = get_movies_dataframe()
    # Turns each string into a Python list
    data['genres'] = data['genres'].str.split(', ')
    # Takes column containing lists and duplicates entire row once per item in list
    exploded_df = data.explode('genres')
    genre_number = exploded_df['genres'].value_counts()

    return genre_number