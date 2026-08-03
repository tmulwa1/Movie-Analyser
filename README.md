# Movie-Analyser
An Flask web app for logging movies you've watched and discovering new ones - a personal movie diary and a genre-based movie discovery tool powered by TMDb.

## Features
- **Personal log** - search TMDb, log movies you've watched with your own rating, notes and date.
- **Discover** - browse movies by genre
- **Where to watch** - see streaming/ rental/ purchase availability in the UK for any movie

## Technologies
- Flask + Jinja2
- SQLAlchemy + SQLite
- TMDb API
- Vanilla JS
- Pandas + Matplotlib

## Setup
1. Clone repository
2. Get free TMDb API key: **https://www.themoviedb.org/settings/api**
3. Create `.env` file in project root (copy .env.example and add your key)
4. Install dependencies: **pip install -r requirements.txt**
5. Run app: **python app.py**
6. Open browser at **http://127.0.0.1:5000**