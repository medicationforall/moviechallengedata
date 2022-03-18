from collect.collectMovies import collect_movies
from collect.collectGenres import collect_genres
from collect.collectTags import collect_tags

def __process_movie_files():
    print('__process_movie_files')

    movies_df = collect_movies()
    movies_df.to_json('out/movies.json', orient="index")

    genres_df = collect_genres()
    genres_df.to_json('out/genres.json', orient="records")

    tags_df = collect_tags()
    tags_df.to_json('out/tags.json', orient="records")

if __name__ == '__main__':
    __process_movie_files()
