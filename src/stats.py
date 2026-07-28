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
    # Converting from object to datetime
    df['date_watched'] = pd.to_datetime(df['date_watched']) 
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

def average_rating_by_genre():
    data = get_movies_dataframe()
    data['genres'] = data['genres'].str.split(', ')
    exploded_df = data.explode('genres')
    average = exploded_df.groupby('genres')['my_rating'].mean()
    return average

def average_rating_by_director():
    data = get_movies_dataframe()
    average = data.groupby('director')['my_rating'].mean()
    return average

def ratings_over_time():
    data = get_movies_dataframe()
    # Converts date into 'year-month' format
    data['month'] = data['date_watched'].dt.to_period('M')
    average = data.groupby('month')['my_rating'].mean()
    return average