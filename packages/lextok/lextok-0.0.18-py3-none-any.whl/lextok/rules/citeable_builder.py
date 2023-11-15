from typing import Any, NamedTuple

from lextok.rules._pattern import _orth_in, _re


class Duo(NamedTuple):
    """Given two letters, create possible patterns using uppercase text."""

    a: str
    b: str

    @property
    def x(self):
        return self.a.upper()

    @property
    def y(self):
        return self.b.upper()

    @property
    def as_token(self) -> dict[str, list[dict[str, str]]]:
        """Used to create special rules for custom tokenizer."""
        return {f"{self.x}.{self.y}.": [{"ORTH": f"{self.x}.{self.y}."}]}

    @property
    def v1(self) -> list[dict[str, str]]:
        # R . A .
        return [{"ORTH": self.x}, {"ORTH": "."}, {"ORTH": self.y}, {"ORTH": "."}]

    @property
    def v2(self) -> list[dict[str, str]]:
        return [{"ORTH": f"{self.x}."}, {"ORTH": f"{self.y}."}]  # R. A.

    @property
    def v3(self) -> list[dict[str, str]]:
        return [{"ORTH": f"{self.x}.{self.y}."}]  # R.A.

    @property
    def v4(self) -> list[dict[str, str]]:
        return [{"ORTH": f"{self.x}{self.y}"}]  # RA

    @property
    def patterns(self) -> list[list[dict[str, str]]]:
        return [self.v1, self.v2, self.v3, self.v4]

    def add_to_each_pattern(self, terminators: list[dict[str, Any]]):
        for p in self.patterns:
            yield p + terminators


class Style(NamedTuple):
    """A `Style` refers to the way a specific two-`let`ter acronym can be used to create
    various letter patterns along with the word variants described in `v`.
    If no `let` exists, will only create word patterns using `v`."""

    v: list[str] = []
    let: str | None = None
    pre: list[str] = ["No", "Nos", "No.", "Nos."]
    r: str = "[\\w-]+"

    @property
    def title_pre(self) -> list[dict[str, Any]]:
        return [_orth_in(self.pre), _re(self.r)]

    @property
    def upper_pre(self) -> list[dict[str, Any]]:
        return [_orth_in([i.upper() for i in self.pre]), _re(self.r)]

    @property
    def token_parts(self):
        """The first pass is for indiscriminate words e.g. `bar matter`; the second, for
        dealing with periods, e.g. `adm. matter`. The first will generate the following as
        token parts ('bar','matter'); the second: ('adm.','matter'), ('adm','.','matter')
        """
        objs = set()
        for words in self.v:
            partial = []
            for word in words.split():
                partial.append(word)
            objs.add(tuple(partial))
        for words in self.v:
            partial = []
            for word in words.split():
                if word.endswith("."):
                    cleaned = word.removesuffix(".")
                    partial.append(cleaned)
                    partial.append(".")
                else:
                    partial.append(word)
            objs.add(tuple(partial))
        return objs

    @property
    def _title_num(self) -> list[list[dict[str, Any]]]:
        return [
            [{"ORTH": sub.title()} for sub in subtokens] + self.title_pre
            for subtokens in self.token_parts
        ]

    @property
    def _title_no_num(self) -> list[list[dict[str, Any]]]:
        return [
            [{"ORTH": sub.title()} for sub in subtokens] + [_re(self.r)]
            for subtokens in self.token_parts
        ]

    @property
    def _upper_num(self) -> list[list[dict[str, Any]]]:
        return [
            [{"ORTH": sub.upper()} for sub in subtokens] + self.upper_pre
            for subtokens in self.token_parts
        ]

    @property
    def _upper_no_num(self) -> list[list[dict[str, Any]]]:
        return [
            [{"ORTH": sub.upper()} for sub in subtokens] + [_re(self.r)]
            for subtokens in self.token_parts
        ]

    @property
    def initials(self) -> Duo | None:
        if not self.let:
            return None
        if len(self.let) != 2:
            return None
        return Duo(a=self.let[0], b=self.let[1])

    @property
    def word_patterns(self) -> list[list[dict[str, Any]]]:
        patterns = []
        patterns.extend(self._title_num)
        patterns.extend(self._title_no_num)
        patterns.extend(self._upper_num)
        patterns.extend(self._upper_no_num)
        return patterns

    @property
    def letter_patterns(self) -> list[list[dict[str, Any]]]:
        items: list[list[dict[str, Any]]] = []
        if not self.initials:
            return items
        for target_nodes in (self.upper_pre, self.title_pre, [_re(self.r)]):
            for b in self.initials.add_to_each_pattern(target_nodes):
                items.append(b)
        return items

    @property
    def patterns(self) -> list[list[dict[str, Any]]]:
        words = self.word_patterns
        letters = self.letter_patterns
        return words + letters if letters else words
