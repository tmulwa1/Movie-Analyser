import requests
from config import TMDB_API_KEY, TMDB_BASE_URL

def search_movies(query):
    url= f"{TMDB_BASE_URL}/search/movie"
    params = {"api_key": TMDB_API_KEY, "query": query}

    # build a response by sending a GET request to API
    response = requests.get(url, params=params)
    data = response.json()

    # extracting the results list from data
    results_list = data['results']

    # slicing to retrieve only top 5 results
    results_list = results_list[:5]

    # creating a list of dictionaries with release_year as its own key
    movie_data = [
        {
            **{key: item[key] for key in ['id', 'title', 'poster_path'] if key in item},
            'release_year': item.get('release_date', '')[:4] if item.get('release_date') else 'N/A'
        }
        for item in results_list
    ]
    return(movie_data)
