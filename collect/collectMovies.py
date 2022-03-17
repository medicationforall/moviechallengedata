from pathlib import Path
import pandas as pd

def collect_movies():
    movies_path = Path('input/movies.csv')
    movies_df = pd.read_csv(movies_path)
    print(movies_df)
    return movies_df
