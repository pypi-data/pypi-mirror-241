from typing import Any

from lextok.rules._pattern import (
    CM,
    COURT,
    OF,
    OF_THE_PH_,
    TH,
    Label,
    Rule,
    _orth_in,
    _re,
    lower_words,
    titled_words,
)
from lextok.rules.abbreviations import CaseName, abbv_months, org_options
from lextok.rules.entity_rules_citeable import num_sym, opt_nums, provs

casename = Rule(label=Label.CaseName, patterns=CaseName.permute_patterns())

date_as_entity = Rule(
    label=Label.DATE,
    patterns=[
        [
            CM | {"OP": "?"},
            {"LOWER": {"IN": ["s.", "series"]}},
            OF | {"OP": "?"},
            _re("\\d{4}"),
        ]
    ]
    + [
        [
            CM | {"OP": "?"},
            {"ORTH": month},
            _orth_in([f"{str(i)}" for i in range(1, 31)]),
            CM | {"OP": "?"},
            _re("\\d{4}"),
        ]
        for month_data in abbv_months
        for month in month_data.value.options
    ],
)
prefix_tits = _orth_in(["Atty.", "Hon.", "Engr.", "Dr.", "Dra."])
prefix_titled_person = Rule(
    label=Label.PERSON,
    patterns=[
        [prefix_tits, {"IS_TITLE": True, "OP": "+"}],
        [prefix_tits, {"ENT_TYPE": Label.PERSON.name}],
    ],
)


juridical_org = Rule(
    label=Label.ORG,
    patterns=[
        [
            {"IS_TITLE": True, "OP": "+"},
            {"ORTH": ",", "IS_PUNCT": True, "OP": "?"},
            {
                "LOWER": {"IN": list(set(o.lower() for o in org_options))},
                "IS_TITLE": True,
            },
        ],
        [{"ORTH": "Estate"}, OF, {"IS_TITLE": True, "OP": "+"}],
        [{"ORTH": "Estate"}, OF, {"ENT_TYPE": Label.PERSON.name}],
    ],
)

generic_laws = Rule(
    label=Label.StatuteNamed,
    patterns=[
        [
            TH,
            _orth_in(["1987", "1973", "1935"]) | {"OP": "?"},
            _orth_in(["CONSTITUTION", "Constitution", "CONST", "Const."]),
        ],
        [{"ORTH": "Rules"}, OF, COURT],
        titled_words("old code"),
        titled_words("philippine civil code"),
        titled_words("civil code of 1950"),
        titled_words("civil code of 1889"),
        titled_words("civil code"),
        titled_words("civil code") + OF_THE_PH_,
        lower_words("revised administrative code of 1987"),
        lower_words("revised administrative code of 1917"),
        lower_words("revised administrative code"),
        lower_words("administrative code of 1987"),
        lower_words("administrative code of 1917"),
        lower_words("administrative code of 1916"),
        lower_words("administrative code"),
        lower_words("admin. code"),
        lower_words("admin code"),
        lower_words("adm. code"),
        lower_words("adm code"),
    ],
)


up = {"IS_UPPER": True, "OP": "+"}
tit = {"IS_TITLE": True, "OP": "+"}
opt_tit = {"IS_TITLE": True, "OP": "*"}

opt_cover = {"TEXT": {"REGEX": "\\(.*\\)"}, "OP": "?"}

doc_variants: list[list[dict[str, Any]]] = [
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
]
generic_documents = Rule(label=Label.Candidate, patterns=doc_variants)
"""Connect a generic serial number with a date, e.g. `Doc No. 414, Jan. 15, 2000`"""


irr_variants: list[list[dict[str, Any]]] = [
    [
        {"LOWER": "rules", "IS_TITLE": True},
        {"LOWER": "and", "IS_LOWER": True},
        {"LOWER": "regulations", "IS_TITLE": True},
        {"LOWER": "implementing", "IS_TITLE": True},
        {"IS_TITLE": True, "OP": "*"},
    ],
    [
        {"LOWER": "implementing", "IS_TITLE": True},
        {"LOWER": "rules", "IS_TITLE": True},
        {"LOWER": "and", "IS_LOWER": True},
        {"LOWER": "regulations", "IS_TITLE": True},
        {"ORTH": {"IN": ["of", "the"]}, "OP": "*"},
        {"IS_TITLE": True, "OP": "*"},
    ],
    [
        {"LOWER": {"IN": ["old", "new", "pre"]}, "IS_LOWER": True, "OP": "?"},
        {"ORTH": "-", "OP": "?"},
        {"SHAPE": "dddd", "OP": "?"},  # 1997, 1964, 2004
        {"IS_UPPER": True, "OP": "*"},  # NLRC, COMELEC, DARAB, Revised
        {"IS_TITLE": True, "OP": "*"},  # Revised
        {"LOWER": {"IN": ["rule", "rules"]}, "IS_TITLE": True},
        {"LOWER": {"IN": ["on", "of"]}},
        {"IS_TITLE": True, "OP": "*"},
    ],
    [
        {"SHAPE": "dddd", "OP": "?"},  # 1997, 1964, 2004
        {"IS_UPPER": True, "OP": "*"},  # NLRC
        {"IS_TITLE": True, "OP": "*"},  # Revised
        {"LOWER": "revised", "OP": "?"},
        {
            "LOWER": {"IN": ["omnibus", "uniform", "implementing", "rules", "interim"]},
            "IS_TITLE": True,
            "OP": "+",
        },
    ],
]
opt_connect: dict[str, Any] = {"ORTH": {"IN": ["of", "the", ","]}, "OP": "*"}

generic_irrs = Rule(label=Label.Candidate, patterns=irr_variants)

prov_irr = Rule(
    label=Label.CandidateProvision,
    patterns=[[provs, opt_connect] + i for i in irr_variants]
    + [[provs, opt_connect] + d for d in doc_variants],
)
