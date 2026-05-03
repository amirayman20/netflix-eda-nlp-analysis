"""
Genre analysis utilities:
- explode genres
- extract top words per genre
- extract top bigrams per genre
"""

from text_cleaning_and_bigrams import get_top_words, get_top_bigrams


def explode_genres(df):
    """
    Split 'listed_in' into individual genres and explode into separate rows.
    """
    df['genre_list'] = df['listed_in'].str.split(',').apply(
        lambda x: [g.strip() for g in x]
    )
    df_exploded = df.explode('genre_list')
    df_exploded = df_exploded.rename(columns={'genre_list': 'genre'})
    return df_exploded


def get_top_genres(df_exploded, n=5):
    """
    Return the top N most frequent genres.
    """
    return df_exploded['genre'].value_counts().head(n).index.tolist()


def get_genre_word_stats(df_exploded, genres, n=20):
    """
    For each genre, return the top N words.
    """
    stats = {}
    for g in genres:
        df_g = df_exploded[df_exploded['genre'] == g]
        stats[g] = get_top_words(df_g['clean_desc'], n)
    return stats


def get_genre_bigram_stats(df_exploded, genres, n=20):
    """
    For each genre, return the top N bigrams.
    """
    stats = {}
    for g in genres:
        df_g = df_exploded[df_exploded['genre'] == g]
        stats[g] = get_top_bigrams(df_g['clean_desc'], n)
    return stats

