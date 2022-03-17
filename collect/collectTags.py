from pathlib import Path
import pandas as pd

def collect_tags():
    tags_path = Path('input/tags.csv')
    tags_df = pd.read_csv(tags_path)
    print(tags_df)

    unique_tags = {}

    for tag in tags_df['tag'].values:
        lower_tag = tag.lower()
        #print(lower_tag)
        if lower_tag not in unique_tags:
            unique_tags[lower_tag] = 1
        else:
            unique_tags[lower_tag] += 1

    unique_tag_df = pd.DataFrame(unique_tags.items(), columns=['name','count'])
    unique_tag_df = unique_tag_df.sort_values(by=['count','name'], ascending=[False, True])

    print(unique_tag_df)

    return unique_tag_df
