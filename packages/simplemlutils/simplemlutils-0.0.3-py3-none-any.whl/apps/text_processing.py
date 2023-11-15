import re
import spacy
from typing import List
from mlutils.utils.textutils import (SpaCyTokenizer, RuleBasedTokenizer)

def bag_of_words(text: str, pattern: str) -> List[str]:
    tokens = re.findall(pattern, text)
    return tokens

if __name__ == '__main__':
    pattern = r'\w+(?:\'\w+)?|[^\w\s]'
    text = 'This is my text to get the tokens from.'

    rule_tokenizer = RuleBasedTokenizer(re_pattern=pattern)
    rule_tokens = rule_tokenizer(text)
    print(rule_tokens)

    nlp = spacy.load("en_core_web_sm")

    spacy_tokenizer = SpaCyTokenizer(nlp=nlp, out_as_strings=True)
    spacy_tokens = spacy_tokenizer(text)
    print(spacy_tokens)
    #tokens = bag_of_words(text=text, pattern=pattern)


    # sorted_tokens = sorted(tokens)
    # print(sorted_tokens)