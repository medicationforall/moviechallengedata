from collect.collectMovies import collect_movies
from collect.collectGenres import collect_genres

def __process_movie_files():
    print('__process_movie_files')

    movies_df = collect_movies()
    genres_df = collect_genres()
    genres_df.to_json('out/genres.json', orient="records")

if __name__ == '__main__':
    __process_movie_files()
