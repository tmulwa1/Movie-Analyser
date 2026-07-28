from flask import Flask, render_template, request, redirect, url_for
from src.database import get_session, initialise_db, Movie
from src.tmdb_client import get_movie_details, search_movies
from src.charts import create_genre_chart
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def dashboard():

    session = get_session() 
    create_genre_chart()
    # Query all movies from the database
    movies = session.query(Movie).all()
    rendered = render_template('dashboard.html', movies=movies)
    session.close()

    return rendered

@app.route('/add', methods=['GET','POST'])
def add_movie():
    # Initialize results to an empty list
    results = []

    if request.method == 'POST':
        # Typed a title and searched for it
        search = request.form.get('query')
        results = search_movies(search)
    return render_template('add_movie.html', results=results)

@app.route('/add/confirm/<int:tmdb_id>', methods=['GET','POST'])
def confirm_movie(tmdb_id):
    # First visit
    if request.method == 'GET':
        details = get_movie_details(tmdb_id)
        return render_template('confirm_movie.html', details=details)
    elif request.method == 'POST':
        details = get_movie_details(tmdb_id) 

        # Retreiving form data, returns string, so need to cast
        my_rating = float(request.form.get('my_rating'))
        notes = request.form.get('notes')
        date_watched = request.form.get('date_watched')
        # Converting the date string to a datetime object
        date = datetime.strptime(date_watched, '%Y-%m-%d').date()

        movie = Movie(tmdb_id=details['tmdb_id'], title=details['title'], 
                      release_year=details['release_year'], genres=details['genres'], 
                      director=details['director'], runtime=details['runtime'], vote_average=details['vote_average'], 
                      poster_path=details['poster_path'], my_rating=my_rating, notes=notes, date_watched=date)

        session = get_session()
        session.add(movie)
        session.commit()
        session.close()

        # Redirect to the dashboard after saving the movie
        return redirect(url_for('dashboard'))

@app.route('/movies', methods=['GET'])
def movie_list():
    session = get_session()
    movies = session.query(Movie).all()
    rendered = render_template('movie_list.html', movies=movies)
    session.close()
    return rendered

@app.route('/movies/<int:movie_id>', methods=['GET'])
def movie_details(movie_id):
    session = get_session()
    movie = session.query(Movie).filter_by(id=movie_id).first()

    # Redirects the user if the movie does not exist in the database
    if movie is None:
        session.close()
        return redirect(url_for('dashboard'))

    rendered = render_template('movie_detail.html', movie=movie)
    session.close()
    return rendered
    
if __name__ == '__main__':
    initialise_db()
    app.run(debug=True)

