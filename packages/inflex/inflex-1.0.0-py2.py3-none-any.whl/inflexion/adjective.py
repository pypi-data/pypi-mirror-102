
import re
from typing import Optional

from term import Term

from adjective_core import (
    is_singular,
    is_plural,
    convert_to_singular,
    convert_to_plural,
)
from noun import Noun


class Adjective(Term):
    def __init__(self, term: str, classical: Optional[bool] = False):
        super().__init__(term, classical)

        self._possessive_regex = re.compile(
            r"\A(.*)'s?\Z", flags=re.IGNORECASE | re.MULTILINE | re.DOTALL
        )
        self._possessive_inflexion = {
            # Term           0TH      1ST      2ND      3RD
            "my": {
                "singular": ["my",    "my",    "your",  "its"],
                "plural":   ["our",   "our",   "your",  "their"],
            },
            "your": {
                "singular": ["your",  "my",    "your",  "its"],
                "plural":   ["your",  "our",   "your",  "their"],
            },
            "her": {
                "singular": ["her",   "my",    "your",  "her"],
                "plural":   ["their", "our",   "your",  "their"],
            },
            "his": {
                "singular": ["his",   "my",    "your",  "his"],
                "plural":   ["their", "our",   "your",  "their"],
            },
            "its": {
                "singular": ["its",   "my",    "your",  "its"],
                "plural":   ["their", "our",   "your",  "their"],
            },
            "our": {
                "singular": ["my",    "my",    "your",  "its"],
                "plural":   ["our",   "our",   "your",  "their"],
            },
            "their": {
                "singular": ["its",   "my",    "your",  "its"],
                "plural":   ["their", "our",   "your",  "their"],
            },
        }

    """
    Override default methods from Term    
    """

    def is_adj(self) -> bool:
        return True

    def is_singular(self) -> bool:
        return is_singular(self.term)

    def is_plural(self) -> bool:
        return is_plural(self.term)

    def singular(self, person: Optional[int] = 0) -> str:
        # Is it possessive form?
        match = self._possessive_regex.match(self.term)
        if match:
            return Noun(match.group(1)).plural() + "'s"
        
        if self.term.lower() in self._possessive_inflexion:
            return self._possessive_inflexion[self.term.lower()]["singular"][person]
        
        return convert_to_singular(self.term)

    def plural(self, person: Optional[int] = 0) -> str:
        # Is it possessive form?
        match = self._possessive_regex.match(self.term)
        if match:
            n = Noun(match.group(1)).plural() + "'s"
            return re.sub(r"s's\Z", "s'", n, flags=re.MULTILINE | re.DOTALL)
        
        if self.term.lower() in self._possessive_inflexion:
            return self._possessive_inflexion[self.term.lower()]["plural"][person]
        
        return convert_to_plural(self.term)


if __name__ == "__main__":
    a = Adjective("typical")
    breakpoint()