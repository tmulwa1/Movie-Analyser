from src.database import get_session, Movie
import pandas as pd
from pandas import DataFrame

# Takes Movie rows and puts them into a dataframe
def get_movies_dataframe():
    session = get_session()
    movies = session.query(Movie).all()

    # List comprehension that builds one dictionary per movie
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

