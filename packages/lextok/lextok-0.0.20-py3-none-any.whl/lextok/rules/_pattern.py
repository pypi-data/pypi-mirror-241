import importlib
import io
import itertools
import re
import string
from collections.abc import Iterator
from enum import Enum, auto
from pathlib import Path
from typing import Any

import inflect
import jsonlines
import roman  # type: ignore
from pydantic import BaseModel, model_serializer
from slugify import slugify
from spacy.tokens import Doc, Span
from spacy.util import filter_spans

camel_case_pattern = re.compile(
    r".+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)"
)


def uncamel(text: str) -> list[str]:
    """For text in camelCaseFormatting, convert into a list of strings."""
    return [m.group(0) for m in camel_case_pattern.finditer(text)]


class Label(Enum):
    """A `Label` is shorthand for creating a spacy `ENT_TYPE` for entity-based patterns
    and `LABEL`s for span patterns. An alternate route would be to use 2 types of
    data structures (one for entities and one for spans) but this adds complexity downstream
    since all `Rule`s will now have to have different label fields rather than just a single one.

    Each member of the `Label` Enum will contain properties and methods:

    1. `@node` to represent `{"ENT_TYPE": <Enum member name>}`
    2. `@opt`: adds `{"OP": "?}` to the `@node`
    3. `@snakecase`: each label gets converted to a snakecased variable that can be used as a custom Doc attribute
    4. `extract_entities(doc)`: get all Spans that are entities a _member_ `Label`
    5. `extract_spans(doc)`: : get all Spans that match a SpanRuler key which is a _member_ `Label`
    """

    ORDINAL = auto()
    PERSON = auto()
    GPE = auto()
    LAW = auto()
    ORG = auto()
    DATE = auto()
    Actor = auto()
    Common = auto()
    GovtDivision = auto()
    CourtName = auto()
    Concept = auto()
    Doctrine = auto()
    Paper = auto()
    ProvisionNum = auto()
    StatuteNum = auto()
    StatuteNamed = auto()
    StatutoryProvision = auto()
    StatutoryLink = auto()
    CaseName = auto()
    DocketNum = auto()
    ReporterNum = auto()
    DecisionCitation = auto()
    GenericNum = auto()
    GenericDocument = auto()

    @property
    def node(self) -> dict[str, str]:
        return {"ENT_TYPE": self.name}

    @property
    def opt(self) -> dict[str, str]:
        return self.node | {"OP": "?"}

    @property
    def snakecase(self) -> str:
        """Used as the variable for spacy's custom attributes e.g. `doc._.provision_nums`"""
        return "_".join(uncamel(self.name)).lower() + "s"

    def extract_entities(self, doc: Doc) -> list[Span]:
        """Generate doc's entities matching a label."""
        return [ent for ent in doc.ents if ent.label_ == self.name]

    def extract_spans(self, doc: Doc) -> list[Span]:
        """Generate doc's span ruler patterns matching a label."""
        return [span for span in filter_spans(doc.spans[self.name])]


SPAN_RULER_LABELS = [
    Label.Actor,
    Label.Concept,
    Label.Paper,
    Label.Doctrine,
    Label.DecisionCitation,
    Label.StatutoryProvision,
    Label.StatutoryLink,
]
"""When included in this list, consider the `Rule` associated with the `Label` a _SpanRuler_ pattern."""


excludables = [Label.DATE, Label.ORDINAL] + SPAN_RULER_LABELS
"""No need to include these in the custom attributes of each Doc."""

ENTITY_RULER_LABELS = [member for member in Label if member not in excludables]
"""When included in this list, consider the `Rule` associated with the `Label` an _EntityRuler_ pattern."""


class Rule(BaseModel):
    """`patterns` associated with a single `label` (optionally
    with an `id` as well that serve as the `ent_id_` in `spacy.tokens.Doc.ents`).
    It can also be used for pattern objects for `spacy.tokens.Doc.spans`. See generally:

    1. https://spacy.io/usage/rule-based-matching#entityruler-files
    2. https://spacy.io/usage/rule-based-matching#spanruler-files

    A `Rule` enables the creation of such pattern objects containing the same `Label` and custom `id`, if provided. Sample rule:

    ```py
    sample = Rule(
        id="ministry-labor",
        label=Label.GovtDivision,
        patterns=[
            [
                {"LOWER": "the", "OP": "?"},
                {"LOWER": "ministry"},
                {"LOWER": "of"},
                {"LOWER": "labor"},
            ]
        ],
    )
    ```

    Use with: <Rule instance>.create_file() or <Rule instance>.model_dump() to
    simply get a list of patterns without file creation. See common usage in
    `set_entity_ruler()`
    """

    id: str | None = None
    label: Label
    patterns: list[list[dict[str, Any]]]

    def __str__(self) -> str:
        return f"<Rule {self.ent_id})>"

    def __repr__(self) -> str:
        return f"<Rule {self.ent_id}: {len(self.patterns)} patterns>"

    @property
    def ent_id(self):
        return self.id or "-".join(uncamel(self.label.name)).lower()

    @model_serializer
    def ser_model(self) -> list[dict[str, Any]]:
        """Following the pydantic convention for .model_dump(); instead of a traditional
        `dict` return, the function results in a serialized list of patterns for consumption
        by either `create_file()` or the _entity_ruler_ spacy pipeline."""
        return [
            {"id": self.ent_id, "label": self.label.name, "pattern": pattern}
            for pattern in self.patterns
        ]

    def create_file(self, file: Path | None = None):
        """Will update the file, if it exists; will create a file, if it doesn't exist."""
        if not file:
            file = Path(__file__).parent.joinpath(f"{self.ent_id}.jsonl")
        fp = io.BytesIO()
        with jsonlines.Writer(fp) as writer:
            for ser_pattern in self.model_dump():
                writer.write(ser_pattern)
        file.unlink(missing_ok=True)
        file.write_bytes(fp.getbuffer())
        return file

    @classmethod
    def extract_from_files(
        cls,
        folder: Path,
        glob_pattern: str = "*.py",
        excluded: tuple = ("__init__", "_pattern", "tester"),
        ents: bool = True,
    ) -> Iterator["Rule"]:
        """If the `Rule` instances found in the folder containg the glob pattern
        have a `.label` value that is True, then the rule should be mapped to the entity ruler;
        else, the rule should be mapped to the span ruler.

        The method of dynamically extracting from files is adopted from:
        https://stackoverflow.com/a/50181975/9081369

        Args:
            ents (bool, optional): See `Label` object whose value is `True` or `False`. Defaults to `True`.

        Yields:
            Iterator[Rule]: Rules that match the `ents` configuration.
        """
        for file in folder.glob(glob_pattern):
            if file.stem not in excluded:
                modules = {}
                spec = importlib.util.spec_from_file_location(file.stem, file)  # type: ignore
                modules[file.stem] = importlib.util.module_from_spec(spec)  # type: ignore
                spec.loader.exec_module(modules[file.stem])  # type: ignore
                for var_name, rule_candidate in modules[file.stem].__dict__.items():
                    if not var_name.startswith("__"):
                        if isinstance(rule_candidate, Rule):
                            if not rule_candidate.id:
                                rule_candidate.id = slugify(var_name)
                            if ents:
                                if rule_candidate.label not in SPAN_RULER_LABELS:
                                    yield rule_candidate
                            else:
                                if rule_candidate.label in SPAN_RULER_LABELS:
                                    yield rule_candidate


def _re(v: str, anchored: bool = True) -> dict[str, Any]:
    """Helper function to add an anchored, i.e. `^`<insert value `v` here>`$`
    regex pattern, following the convention `{"TEXT": {"REGEX": f"^{v}$"}}`
    spacy convention.
    """
    if anchored:
        v = f"^{v}$"
    return {"TEXT": {"REGEX": v}}


def _orth_in(v_list: list[str]):
    """Helper function to add a regex pattern where the options contained
    in the `v_list` are limited, following the convention `{"ORTH": {"IN": v_list}}`
    spacy convention.
    """
    return {"ORTH": {"IN": v_list}}


def _multi(pattern: list[dict[str, Any]], count: int) -> list[list[dict[str, Any]]]:
    """Create cumulative `pattern`s based on the `count` indicated.
    e.g. `repeat_pattern([1,2])` results in:

    [
        [1, 2],
        [1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1, 2],
        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    ]
    ```
    """
    res: list[list[dict[str, Any]]] = []
    res.append(pattern)
    for i in range(count):
        added = pattern + res[-1]
        res.append(added)
    return res


# REUSABLES


OF = {"LOWER": "of"}
"""Required `the`: `{"LOWER": "of"}`"""

TH = {"LOWER": "the", "OP": "?"}
"""Optional `the`: `{"LOWER": "the", "OP": "?"}`"""

COURT = {"ORTH": "Court"}
"""Required title cased `Court`"""

CODE = {"ORTH": "Code"}
"""Required title cased `Code`"""

THE = {"LOWER": "the"}
"""Required `the`: `{"LOWER": "the"}`"""

VS = _orth_in(["v.", "vs."])
"""Common formula for consistency: `{"ORTH": {"IN": ["v.", "vs."]}}`"""

PH = _orth_in(["Phil", "Phil.", "Phils", "Phils.", "Philippines"])

CM = {"ORTH": ","}

OF_THE_PH_ = [OF, THE, PH]

CONNECTOR = _orth_in(["of", "the", ",", "and", "&"]) | {"OP": "*"}
"""Setting this optional token ("of", "the", ",", "and", "&") allows for
ProvisionNums/serials to be merged later"""

### PATTERN FUNCS


def lower_words(words: str):
    """Will separate each word separated by spaces into a
    `{"LOWER": <word.strip().lower()>}` spacy pattern."""
    return [{"LOWER": word.strip().lower()} for word in words.split()]


def titled_words(words: str):
    """Will separate each word separated by spaces into a
    `{"LOWER": <word.lower()>, "IS_TITLE": True}` spacy pattern."""
    return [w | {"IS_TITLE": True} for w in lower_words(words)]


def name_code(fragments: str):
    """Use of `lower_words()` for Code names"""
    return [TH, {"LOWER": "code"}, OF] + lower_words(fragments)


def name_court(fragments: str):
    """Create title-based Court names"""
    return [TH, COURT, OF] + titled_words(fragments)


def name_statute(
    fragments: str | list[dict[str, Any]],
    options: list[str] = ["law", "act"],
) -> list[dict[str, Any]]:
    """If a string is passed as fragments, uses `lower_words()`
    in between options for named laws; if what is passed is a list of
    these same spacy patterns, these will be added as options."""
    bits: list[dict[str, Any]] = [TH]
    if isinstance(fragments, str):
        bits.extend(lower_words(fragments))
    elif isinstance(fragments, list):
        bits.extend(fragments)
    bits.append({"LOWER": {"IN": options}, "IS_TITLE": True})
    return bits


## DIGITS


p = inflect.engine()

roman_upper = [roman.toRoman(i) for i in range(1, 100)]
a_z_lower = [i for i in string.ascii_lowercase]
pairs = itertools.combinations_with_replacement(a_z_lower, r=2)
aa_zz_lower = [f"{a}{b}" for a, b in pairs]


class DigitLists(Enum):
    HundredDigit = [str(i) for i in range(0, 100)]
    WordHundredDigit = [p.number_to_words(num=i) for i in range(1, 100)]  # type: ignore
    RomanHundredLower = [i.lower() for i in roman_upper]
    RomanHundredUpper = [roman.toRoman(i) for i in range(1, 100)]
    AtoZSingleLower = a_z_lower
    AtoZSingleUpper = [i.upper() for i in a_z_lower]
    AtoZDoubleLower = aa_zz_lower
    AtoZDoubleUpper = [i.upper() for i in aa_zz_lower]

    @classmethod
    def generate_options(cls) -> list[str]:
        options: list[str] = []
        for member in cls:
            options.extend(member.value)  # type: ignore
        return options


HAS_DIGIT = _re(v=".*\\d.*")
"""Any token containing a digit should be used in tandem with an attribute ruler."""

IS_COVERED = _re(v=".*\\(\\w{1,2}\\).*")
"""Any token containing a digit should be used in tandem with an attribute ruler."""

SPECIFIC = _re("(" + "|".join(DigitLists.generate_options()) + ")")
"""Any token matching the options created by DigitLists"""

IS_ROMAN = _re(v="[IXV]+[-\\.][A-Z]{1,2}")
"""Handle combinations like I-A"""

PROV_DIGITS = [SPECIFIC, HAS_DIGIT, IS_COVERED, IS_ROMAN]
