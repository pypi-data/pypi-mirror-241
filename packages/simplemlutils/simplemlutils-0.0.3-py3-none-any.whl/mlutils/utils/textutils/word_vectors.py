from typing import List, Tuple, Callable
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def compute_word_count_vector(corpus: List[str]) -> List:
    vectorizer = CountVectorizer()
    vector = vectorizer.fit_transform(corpus)
    return vector.toarray()

def compute_ngram_vector(corpus: List[str], n_gram: Tuple[int, int]) -> List:
    vectorizer = CountVectorizer(ngram_range=n_gram)
    vector = vectorizer.fit_transform(corpus)
    return vector.toarray()

def compute_tfidf_vector(corpus: List[str], min_df: int=1) -> List:
    vectorizer = TfidfVectorizer(min_df=min_df)
    vector = vectorizer.fit_transform(corpus)
    return vector.toarray()

def compute_tfidf_vector_with_tokenizer(corpus: List[str], tokenizer: Callable) -> List:
    vectorizer = TfidfVectorizer(tokenizer=tokenizer)
    vector = vectorizer.fit_transform(raw_documents=corpus)
    return vector.toarray()


