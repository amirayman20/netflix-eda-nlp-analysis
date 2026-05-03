"""
Text cleaning + word frequency + bigram extraction utilities
Used across the Netflix NLP pipeline.
"""

import re
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from config import STOPWORDS


def clean_text(text):
    """
    Clean raw text by:
    - converting to lowercase
    - removing punctuation/symbols
    - removing stopwords
    - keeping words longer than 2 characters
    """
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)

    words = text.split()
    words = [w for w in words if w not in STOPWORDS and len(w) > 2]

    return " ".join(words)


def get_top_words(text_series, n=20):
    """
    Return the top N most frequent words in a cleaned text series.
    """
    all_words = " ".join(text_series).split()
    return Counter(all_words).most_common(n)


def get_top_bigrams(text_series, n=20):
    """
    Extract the top N bigrams using CountVectorizer.
    """
    vectorizer = CountVectorizer(ngram_range=(2, 2))
    X = vectorizer.fit_transform(text_series)

    bigram_counts = X.sum(axis=0).A1
    bigram_names = vectorizer.get_feature_names_out()

    bigram_freq = sorted(
        list(zip(bigram_names, bigram_counts)),
        key=lambda x: x[1],
        reverse=True
    )

    return bigram_freq[:n]
