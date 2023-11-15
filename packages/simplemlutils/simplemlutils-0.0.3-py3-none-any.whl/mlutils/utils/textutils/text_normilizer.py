from typing import List, Callable

def normalize_tokens(tokens: List[str]) -> List[str]:
    return [x.lower() for x in tokens]

def normalize_text(text: str, first_word_only: bool,
                   tokenizer: Callable) ->str:

    if not first_word_only:
        return text.lower()

    # get the first word in the text
    tokens = tokenizer(text)
    tokens[0] = tokens[0].lower()

    return "".join(tokens)