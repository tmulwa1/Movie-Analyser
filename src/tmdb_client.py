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

def get_movie_details(tmdb_id):
    url= f"{TMDB_BASE_URL}/movie/{tmdb_id}"
    params = {"api_key": TMDB_API_KEY, "append_to_response": "credits"} # append_to_response lets you bundle credits data into the same request

    # build a response by sending a GET request to API
    response = requests.get(url, params=params)
    data = response.json()

    # extracting the relevant data from the response
    movie_genres = str.join(', ', [genre['name'] for genre in data['genres']])
    # for loop to find the director's name in the credits data
    movie_director = next((crew_member['name'] for crew_member in data['credits']['crew'] if crew_member['job'] == 'Director'), None)

    movie_data = {
        'title': data.get('title', 'N/A'),
        'tmdb_id': data.get('id', 'N/A'),
        'runtime': data.get('runtime', 'N/A'), 
        'release_year': data.get('release_date', '')[:4] if data.get('release_date') else 'N/A',
        'genres': movie_genres,
        'director': movie_director,
        'vote_average': data.get('vote_average', 'N/A'),
        'poster_path': data.get('poster_path', None)
    }
    return movie_data

def get_genres():
    url= f"{TMDB_BASE_URL}/genre/movie/list"
    params = {"api_key": TMDB_API_KEY}
    response = requests.get(url, params=params)
    data = response.json()
    results_list = data['genres']
    return results_list

def discover_movies_by_genre(genre_id):
    url= f"{TMDB_BASE_URL}/discover/movie"
    params = {"api_key": TMDB_API_KEY, "with_genres": genre_id}
    response = requests.get(url, params=params)
    data = response.json()
    results_list = data['results']
    return results_list

def get_watch_providers(tmdb_id):
    url= f"{TMDB_BASE_URL}/movie/{tmdb_id}/watch/providers"
    params ={"api_key": TMDB_API_KEY}
    response = requests.get(url, params=params)
    data = response.json()
    results_list = data['results']
    return results_list.get('GB', {})