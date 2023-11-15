"""module spacy_tokenizer. Simple class that
wraps spaCy tokens

"""
from typing import List, Union
from spacy import Language
from spacy.tokens import Token


class SpaCyTokenizer(object):
    def __init__(self, nlp: Language, out_as_strings: bool = True):
        self.nlp = nlp
        self.out_as_strings = out_as_strings

    def __call__(self, document: str) -> Union[List[str], List[Token]]:

        tokens = self.nlp(document)

        if self.out_as_strings:
            tokens = [token.text for token in tokens]
        return tokens
