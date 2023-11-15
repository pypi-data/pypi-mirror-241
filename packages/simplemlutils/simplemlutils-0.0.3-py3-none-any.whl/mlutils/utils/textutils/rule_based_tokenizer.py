"""module rule_based_tokenizer. Simple class
that models a tokenizer using regular expression

"""

import re

from typing import List

class RuleBasedTokenizer(object):
    def __init__(self, re_pattern: str):
        self.re_pattern = re_pattern

    def __call__(self, text: str) -> List[str]:
        return list(re.findall(self.re_pattern, text))