import requests
from data_ip import MovieDatabase

class MoviePosterDownloader:
    def __init__(self, api_key):
        self.api_key = api_key

    def search_movie(self, movie_title):
        response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={self.api_key}&query={movie_title}')

        if response.status_code == 200:
            search_results = response.json()['results']
            return search_results
        else:
            return []

    def download_poster(self, movie_id, poster_path):
        poster_url = f'https://image.tmdb.org/t/p/original{poster_path}'
        response = requests.get(poster_url)

        if response.status_code == 200:
            filename = f'{movie_id}.jpg'
            with open(filename, 'wb') as f:
                f.write(response.content)
            return filename
        else:
            return None

    def add_to_mongo(self, movie_title,movie_db):
        search_results = self.search_movie(movie_title)

        if len(search_results) > 0:
            first_result = search_results[0]
            poster_path = first_result['poster_path']
            movie_id = first_result['id']

            filename = self.download_poster(movie_id, poster_path)

            if filename:
                movie_db.add_data(movie_title, filename, movie_id, f'https://image.tmdb.org/t/p/original{poster_path}')
                return True
            else:
                print('Unable to download poster image')
        else:
            print('No search results found')

        return False

# Usage example
if __name__ == "__main__":
    print("hi")
