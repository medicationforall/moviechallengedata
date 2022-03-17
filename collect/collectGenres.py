from pathlib import Path
import pandas as pd

def collect_genres():
    movies_path = Path('input/movies.csv')
    movies_df = pd.read_csv(movies_path)
    genres = movies_df['genres']
    unique_genres = {}

    for value in genres.values:
        # print(value);
        genre_split = value.split('|')

        for genre in genre_split:
            if genre not in unique_genres:
                unique_genres[genre] = 1
            else:
                unique_genres[genre] += 1

    genre_df = pd.DataFrame(unique_genres.items(), columns=['name','count'])
    genre_df = genre_df.sort_values(by=['name'])

    #print(genre_df)

    return genre_df
