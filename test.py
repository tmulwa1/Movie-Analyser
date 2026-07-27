from src.database import initialise_db, get_session, Movie
from src.tmdb_client import get_movie_details
from datetime import date

initialise_db()
details = get_movie_details(27205)  

movie = Movie(
    tmdb_id=details['tmdb_id'], title=details['title'], release_year=details['release_year'],
    genres=details['genres'], director=details['director'], runtime=details['runtime'], vote_average=details['vote_average'], poster_path=details['poster_path'], my_rating=8.0, notes="Great movie!", date_watched=date(2026, 7, 24))

session = get_session()
session.add(movie)
session.commit()
session.close()

# Debugging
print("Saved!")