from typing import Dict, List, Callable, Tuple, Any
from collections import Counter
import pandas as pd

class BagOfWords(object):
    """class BagOfWords maintains a dictionary
    of terms these are the keys of the dictionary and the
    number of instances the key term has been identified in the
    text that is used to populate the bag

    """

    def __init__(self):

        # the actual bag. Maint
        self.bow: Dict = {}

    def __len__(self):
        return len(self.bow)

    def add_tokens(self, tokens: List[str]) -> None:
        """Add tokens to the bag

        Parameters
        ----------
        tokens: The tokens to add in the bag

        Returns
        -------
        None
        """

        for token in tokens:
            if token in self.bow:
                self.bow[token] += 1
            else:
                self.bow[token] = 1

    def add_text(self, text: str, tokenizer: Callable) -> None:
        tokens = tokenizer(text)
        self.add_tokens(tokens=tokens)

    def as_pandas_df(self, fill_na: bool = True) -> pd.DataFrame:
        df = pd.DataFrame(self.bow, index=[0])

        if fill_na:
            df = df.fillna(0).astype(int)

        return df

    def most_common(self, n: int) -> List[Tuple[Any, int]]:
        return Counter(self.bow).most_common(n)