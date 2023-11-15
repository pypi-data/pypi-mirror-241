from collections.abc import Iterator
from enum import Enum
from typing import Any

from lextok.rules._pattern import (
    CM,
    CONNECTOR,
    COURT,
    DigitLists,
    Label,
    Rule,
    _multi,
    _orth_in,
    _re,
    name_court,
    titled_words,
)
from lextok.rules.abbreviations import Prov
from lextok.rules.citeable_builder import Style


class ReporterNum(Enum):
    scra = ["SCRA"]
    phil = ["Phil.", "Phil"]
    og = ["OG", "O.G.", "Off. Gaz."]


reporter_nums = Rule(
    label=Label.ReporterNum,
    patterns=[
        [{"LIKE_NUM": True}, {"ORTH": style}, {"LIKE_NUM": True}]
        for member in ReporterNum
        for style in member.value
    ],
)


class CourtName(Enum):
    SC = [{"LOWER": "supreme", "IS_TITLE": True}, COURT]
    RTC = titled_words("regional trial court")
    CA = name_court("appeals")
    CFI = name_court("first instance")
    MeTC = titled_words("metropolitan trial court")
    MCTC = titled_words("municipal circuit court")
    MTC = titled_words("municipal trial court")
    MTCC = (
        titled_words("municipal trial court")
        + [{"LOWER": "in"}]
        + titled_words("the cities")
    )


court_names = Rule(label=Label.CourtName, patterns=[mem.value for mem in CourtName])  # type: ignore


class DocketNum(Enum):
    GR = Style(let="gr")
    AM = Style(
        let="am",
        v=[
            "adm mat",
            "adm. mat",
            "adm mat.",
            "adm. mat.",
            "adm matter",
            "adm. matter",
            "admin. matter",
            "admin matter",
            "administrative matter",
        ],
    )
    AC = Style(
        let="ac",
        v=[
            "adm case",
            "adm. case",
            "admin. case",
            "admin case",
            "administrative case",
        ],
    )
    BM = Style(let="bm", v=["bar mat.", "bar matter"])


ENT_DOCKET_NUM = Rule(
    label=Label.DocketNum, patterns=[p for mem in DocketNum for p in mem.value.patterns]
)


class StatuteNum(Enum):
    RA = Style(let="ra", r="\\d{1,5}", v=["republic act", "rep. act"])
    CA = Style(let="ca", r="\\d{1,3}", v=["commonwealth act", "com. act"])
    BP = Style(let="bp", r="\\d{1,3}(-?(A|B))?", v=["batas pambansa"], pre=["Blg."])
    EO = Style(let="eo", r="\\d{1,4}(-?(A|B|C))?", v=["executive order", "exec. order"])
    PD = Style(
        let="pd",
        r="\\d{1,4}(-?(A|B))?",
        v=["presidential decree", "pres. decree", "pres. dec."],
    )
    ACT = Style(r="\\d{1,4}", v=["act"])


statute_nums = Rule(
    label=Label.StatuteNum,
    patterns=[p for mem in StatuteNum for p in mem.value.patterns],
)


class ProvisionNum(Enum):
    """A statute's text is divided into (sometimes hierarchical) provisions.
    This structure combines both the adjective division, e.g. `Sec.`, `Section`, `Bk.`, etc.
    (which may have different casing and abbreviations) with presumed valid serial numbers,
    e.g. `1`, `1-b`, `III`, etc.
    """

    abbreviated_Sec1 = list(Prov.set_abbvs())
    abbreviated_sec1 = list(Prov.set_abbvs(cased="lower"))
    abbreviated_SEC1 = list(Prov.set_abbvs(cased="upper"))
    Section1 = list(Prov.set_fulls())
    section1 = list(Prov.set_fulls(cased="lower"))
    SECTION1 = list(Prov.set_fulls(cased="upper"))

    @classmethod
    def generate(cls) -> Iterator[list[dict[str, Any]]]:
        specific_digits = _re("(" + "|".join(DigitLists.generate_options()) + ")")
        for member in cls:
            for end in [{"POS": "NUM"}, specific_digits]:
                start = [CONNECTOR]  # start
                if member.name.startswith("abbreviated_"):
                    yield start + [_orth_in(member.value), {"ORTH": "."}, end]
                    yield start + [_orth_in([f"{v}." for v in member.value]), end]
                yield start + [_orth_in(member.value), end]


special_clauses: list[dict[str, Any]] = [
    Label.ORDINAL.opt,
    {"LOWER": {"IN": ["whereas"]}},
    {"LOWER": {"IN": ["clause", "clauses"]}},
]
provision_nums = Rule(
    label=Label.ProvisionNum, patterns=list(ProvisionNum.generate()) + [special_clauses]
)

# SpanRuler Candidates

up = {"IS_UPPER": True, "OP": "+"}
tit = {"IS_TITLE": True, "OP": "+"}
opt_tit = {"IS_TITLE": True, "OP": "*"}
num_sym = _orth_in(["No", "Nos", "No.", "Nos."])
opt_cover = {"TEXT": {"REGEX": "\\(.*\\)"}, "OP": "?"}
opt_nums = {"POS": {"IN": ["NUM", "PUNCT"]}, "OP": "*"}

ENT_GENERIC_NUM = Rule(
    label=Label.GenericNum,
    patterns=[[num_sym, {"POS": "NUM"}]],
)
"""Create a generic serial number pattern which hasn't been previously defined as an entity."""


generic_documents = Rule(
    label=Label.GenericDocument,
    patterns=[
        [up, tit, opt_cover, Label.GenericNum.node, opt_nums, Label.DATE.node],
        [up, opt_cover, Label.GenericNum.node, opt_nums, Label.DATE.node],
        [tit, opt_cover, Label.GenericNum.node, opt_nums, Label.DATE.node],
        [up, tit, opt_cover, Label.GenericNum.node],
        [up, opt_cover, Label.GenericNum.node],
        [tit, opt_cover, Label.GenericNum.node],
        [up, tit, Label.GenericNum.node],
        [up, Label.GenericNum.node],
        [tit, Label.GenericNum.node],
        [Label.ORG.node, Label.GenericNum.node],
    ],
)
"""Connect a generic serial number with a date, e.g. `Doc No. 414, Jan. 15, 2000`"""


provs = {"ENT_TYPE": Label.ProvisionNum.name, "OP": "+"}
stat = {
    "ENT_TYPE": {
        "IN": [
            Label.StatuteNamed.name,
            Label.StatuteNum.name,
            Label.DocketNum.name,
            Label.GenericNum.name,
        ]
    }
}
opt_comma = CM | {"OP": "?"}
opt_comma_plus = {"ORTH": {"IN": ["of", "the", ","]}, "OP": "*"}

linker = {"ORTH": {"IN": ["or", "and", ",", "&"]}, "OP": "+"}

multi_linked_statute_pattern = _multi([linker, stat], 10)  # type: ignore
for linked_list in multi_linked_statute_pattern:
    linked_list.insert(0, stat)
as_amended: list[dict[str, Any]] = [
    {"ORTH": ",", "IS_PUNCT": True, "OP": "?"},
    {"LOWER": "as", "OP": "?"},
    {"LOWER": "amended"},
    {"LOWER": "by", "OP": "?"},
]

linked_statutes = Rule(
    label=Label.StatutoryLink,
    patterns=multi_linked_statute_pattern + [[stat] + as_amended + [stat]],
)
"""Connect statutory numbers together: `RA 141, RA 4124, RA 5325`"""

statutory_provisions = Rule(
    label=Label.StatutoryProvision,
    patterns=[
        [provs, opt_comma_plus, stat],
        [provs, opt_comma_plus, stat],
        [stat, opt_comma_plus, provs],
    ],
)
"""Connect statutes with provisions: `Art. 2, Civil Code`"""

decision_citations = Rule(
    label=Label.DecisionCitation,
    patterns=[
        [
            Label.CaseName.opt,
            Label.DocketNum.node,
            opt_nums,
            Label.DATE.node,
            opt_comma,
            Label.ReporterNum.node,
        ],
        [
            Label.CaseName.opt,
            Label.DocketNum.node,
            opt_nums,
            Label.DATE.node,
        ],
        [
            Label.CaseName.node,
            Label.ReporterNum.node,
            opt_nums,
            opt_comma,
            Label.DATE.node,
        ],
    ],
)
"""Connect decision names, docket citations, date, and/or reporter numbers: `X v. Y, GR No. 3425, Jan. 1, 2000, 14 SCRA 14`"""
