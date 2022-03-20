from pathlib import Path
import pandas as pd

def collect_movies():
    movies_df = __load_and_clean_movies()

    links_path = Path('input/links.csv')
    links_df = pd.read_csv(links_path, dtype={'imdbId':str,'tmdbId':str})

    #merge movies to links
    movies_links_df = movies_df.merge(links_df, on='movieId')
    movies_links_df = movies_links_df.set_index(['title'])

    movie_tags_df = __build_tags_per_movie()
    movies_links_tags_df = movies_links_df.merge(movie_tags_df, on='movieId')
    movies_links_tags_df.rename(columns={"tag": "tags"}, inplace=True)

    print(movies_links_tags_df)

    return movies_links_tags_df

def __load_and_clean_movies():
        movies_path = Path('input/movies.csv')
        movies_df = pd.read_csv(movies_path)

        # order matters you have to grab the year before you can remove it from the title.
        movies_df['originalTitle'] = movies_df['title']
        movies_df['year'] = movies_df['title'].apply(__parse_year_from_title)
        movies_df['title'] =  movies_df['title'].apply(__remove_year_from_title)
        movies_df = movies_df.sort_values(by=['title'])

        # The data has duplicates!
        # movies_df = movies_df.set_index(['originalTitle'])
        # dupes_movies_df = movies_df[movies_df.index.duplicated(keep=False)]
        # dupes_movies_df.to_csv('out/dupe_movies.csv')

        # drop the duplicates
        movies_df = movies_df.drop_duplicates(subset=['title'])
        return movies_df

def __remove_year_from_title(title):
    '''
        Example title "Bungo Stray Dogs: Dead Apple (2018)"
        returns  "Bungo Stray Dogs: Dead Apple"
        Note* not all titles include the (NNNN) year
    '''
    if ')' in title and '(' in title:
        return title[0:-7]
    else:
        return title

def __parse_year_from_title(title):
    '''
        Example title "Bungo Stray Dogs: Dead Apple (2018)"
        returns  "2018"
        Note* not all titles include the (NNNN) year
    '''
    if ')' in title and '(' in title:
        year = title[-5:-1]
        return year
    else:
        return None

def __build_tags_per_movie():
    tags_path = Path('input/tags.csv')
    tags_df = pd.read_csv(tags_path)
    tags_df.drop(columns=['userId','timestamp'], inplace=True)

    # https://stackoverflow.com/questions/22219004/how-to-group-dataframe-rows-into-list-in-pandas-groupby
    movie_tags_seies = tags_df.groupby('movieId')['tag'].apply(list)
    movie_tags_df = movie_tags_seies.to_frame()

    return movie_tags_df
