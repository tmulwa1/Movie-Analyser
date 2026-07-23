from dotenv import load_dotenv
import os

load_dotenv() # reads .env file into environment

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_BASE_URL = "https://api.themoviedb.org/3"