from flask import Flask, render_template, request, redirect, url_for
from src.database import get_session, initialise_db, Movie
from src.tmdb_client import get_movie_details, search_movies

app = Flask(__name__)

@app.route('/')
def dashboard():

    session = get_session() 
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

if __name__ == '__main__':
    initialise_db()
    app.run(debug=True)

