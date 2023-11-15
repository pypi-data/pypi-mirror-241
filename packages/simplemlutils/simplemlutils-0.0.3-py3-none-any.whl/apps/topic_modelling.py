import numpy as np
from pathlib import Path
import pandas as pd
import spacy
from mlutils.utils.textutils import SpaCyTokenizer
from mlutils.utils.textutils import compute_tfidf_vector_with_tokenizer

pd.options.display.width = 120

DATA_DIR = Path('../data/nlp/toxic_comment_small.csv')

if __name__ == '__main__':


    comments = pd.read_csv(DATA_DIR)
    index = ['comment{}{}'.format(i, '!' * j) for (i, j) in zip(range(len(comments)), comments.toxic)]
    comments = pd.DataFrame(comments.values, columns=comments.columns, index=index)
    mask = comments.toxic.astype(bool).values
    comments['toxic'] = comments.toxic.astype(int)
    print(len(comments))
    print(comments.toxic.sum())
    comments.head(6)

    nlp = spacy.load("en_core_web_sm")
    tokenizer = SpaCyTokenizer(nlp=nlp)

    tfidf_vector = compute_tfidf_vector_with_tokenizer(corpus=comments.text, tokenizer=tokenizer)
    print(f"TF-IDF vector shape {tfidf_vector.shape}")