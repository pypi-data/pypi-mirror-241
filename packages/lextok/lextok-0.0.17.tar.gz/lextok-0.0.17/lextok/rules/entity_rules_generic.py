from ._pattern import (
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
from .abbreviations import CaseName, abbv_months, org_options

ENT_CASE_NAME = Rule(
    label=Label.CaseName,
    patterns=CaseName.permute_patterns(),
)

ENT_CUSTOM_DATE = Rule(
    id="ent-date",
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

ENT_REASONABLE_MAN = Rule(
    id="reasonable-man",
    label=Label.Concept,
    patterns=[
        lower_words("reasonable care and caution"),
        lower_words("a prudent and reasonable man"),
        lower_words("a reasonably discreet and prudent man"),
        lower_words("a person of ordinary caution and prudence"),
        [
            {"LOWER": {"IN": ["person", "man"]}},
            {"LOWER": "of"},
            {"LOWER": "ordinary"},
            {"LOWER": {"IN": ["prudence", "caution", "intelligence"]}},
        ],
        [
            {"LOWER": {"IN": ["ordinary", "ordinarily", "reasonably"]}},
            {"LOWER": {"IN": ["reasonable", "prudent", "cautious"]}},
            {"LOWER": {"IN": ["and", "intelligent", "cautious"]}, "OP": "*"},
            {"LOWER": {"IN": ["man", "person"]}},
        ],
    ],
)

ENT_GENERIC_PERSONALITY = Rule(
    id="generic-personality",
    label=Label.Personality,
    patterns=[
        [
            {"LOWER": "non", "OP": "?"},
            {"ORTH": "-", "OP": "?"},
            {"LOWER": {"IN": ["resident", "nonresident"]}},
            {"LEMMA": {"IN": ["citizen", "alien"]}},
        ],
        [
            {
                "LOWER": {
                    "IN": [
                        "registered",
                        "actual",
                        "absolute",
                        "real",
                        "unregistered",
                        "true",
                    ]
                }
            },
            {"LEMMA": "owner"},
        ],
        [
            {"LEMMA": {"IN": ["estate", "heir"]}, "OP": "?"},
            {"LOWER": {"IN": ["of", "the"]}, "OP": "+"},
            {"LEMMA": {"IN": ["deceased", "decedent"]}},
        ],
        [
            {"LEMMA": {"IN": ["deceased", "decedent"]}},
            {"ORTH": "'s", "OP": "?"},
            {"LEMMA": {"IN": ["spouse", "heir", "estate"]}},
        ],
        [
            {"LOWER": {"IN": ["third", "interested"]}},
            {"LEMMA": {"IN": ["party", "person"]}},
        ],
        [
            {"LOWER": {"IN": ["trial", "appellate", "regular", "lower", "inferior"]}},
            {"LEMMA": "court"},
        ],
    ],
)

ENT_GENERIC_COMMON_TERMS = Rule(
    id="generic-phrases",
    label=Label.Common,
    patterns=[
        [
            {"LOWER": {"IN": ["ex", "pro"]}},
            {"ORTH": "-", "OP": "?"},
            {"LOWER": {"IN": ["parte", "forma"]}},
            {"LOWER": {"IN": ["motion", "rule"]}},
        ],
        [
            {"LOWER": {"IN": ["court", "judicial"]}},
            {"LEMMA": "record"},
        ],
        [
            {"LOWER": "case"},
            {"LOWER": "at"},
            {"LOWER": {"IN": ["bar", "bench"]}},
        ],
        [
            {"LOWER": {"IN": ["back", "monthly"]}},
            {"LEMMA": "rental"},
        ],
        [
            {"LOWER": {"IN": ["insurance", "company"]}},
            {"LEMMA": "policy"},
        ],
        [
            {"LOWER": "certified"},
            {"LOWER": {"IN": ["as", "a"]}, "OP": "*"},
            {"LOWER": "true"},
            {"LEMMA": "copy", "POS": "NOUN"},
        ],
        lower_words("rule of law"),
        lower_words("court of business"),
        [{"LOWER": "multiplicity"}, OF, {"LOWER": {"IN": ["action", "suits"]}}],
        [{"LOWER": "ipso"}, {"LOWER": {"IN": ["facto", "jure"]}}],
        [{"LOWER": {"IN": ["natural", "substantial"]}}, {"LOWER": "justice"}],
        [
            {"LOWER": {"IN": ["affected", "impressed"]}},
            {"LOWER": "with"},
            {"LOWER": "public"},
            {"LOWER": {"IN": ["interest", "trust"]}},
        ],
        [
            {"LOWER": "certain"},
            {"LOWER": {"IN": ["form", "formalities"]}},
            {"LOWER": {"IN": ["may", "be"]}, "OP": "*"},
            {"LOWER": "prescribed"},
            {"LOWER": "by"},
            {"LOWER": "law"},
        ],
        [
            {"LEMMA": {"IN": ["reason", "contrary", "consideration", "matter"]}},
            {"LOWER": {"IN": ["of", "to"]}},
            {"LOWER": "public"},
            {"LOWER": "policy"},
        ],
        [
            {"LOWER": {"IN": ["movable", "immovable", "real", "personal"]}},
            {"LEMMA": "property"},
        ],
        [{"LOWER": "promissory"}, {"LEMMA": "note"}],
        [
            {"LOWER": {"IN": ["mere", "useless"]}},
            {"LOWER": {"IN": ["piece", "scrap"]}},
            {"LOWER": "of"},
            {"LOWER": "paper"},
        ],
        [
            {"LOWER": {"IN": ["government", "public"]}},
            {"LEMMA": {"IN": ["expenditure", "revenue", "fund"]}},
        ],
        [
            {
                "LOWER": {
                    "IN": [
                        "extrinsic",
                        "intrinsic",
                        "collateral",
                        "positive",
                        "actual",
                        "constructive",
                    ]
                }
            },
            {"LOWER": "fraud"},
        ],
        [
            {"LOWER": {"IN": ["good", "bad"]}},
            {"LOWER": "faith"},
        ],
    ],
)

ENT_GENERIC_DECISION_PARTS = Rule(
    id="generic_decision_parts",
    label=Label.Concept,
    patterns=[
        [{"LOWER": "statement"}, {"LOWER": "of"}, {"LEMMA": {"IN": ["fact", "issue"]}}],
        [{"LOWER": "assignment"}, {"LOWER": "of"}, {"LEMMA": "error"}],
        [
            {"LOWER": "dispositive"},
            {"LOWER": {"IN": ["portion", "part"]}},
            {"LOWER": "of", "OP": "?"},
            {"LOWER": "the", "OP": "?"},
            {"LOWER": {"IN": ["decision", "judgment", "case"]}, "OP": "?"},
        ],
        [{"LOWER": "ratio"}, {"LOWER": {"IN": ["legis", "decidendi"]}}],
        [{"LOWER": "obiter"}, {"LOWER": {"IN": ["dictum", "dicta"]}, "OP": "?"}],
    ],
)


ENT_GENERIC_PERSON_PREFIX = Rule(
    id="titled",
    label=Label.PERSON,
    patterns=[
        [
            _orth_in(["Atty.", "Hon.", "Engr.", "Dr.", "Dra."]),
            {"IS_TITLE": True, "OP": "+"},
        ],
        [
            _orth_in(["Atty.", "Hon.", "Engr.", "Dr.", "Dra."]),
            {"ENT_TYPE": Label.PERSON.name},
        ],
    ],
)


ENT_GENERIC_ESTATE = Rule(
    id="estate",
    label=Label.ORG,
    patterns=[
        [{"ORTH": "Estate"}, OF, {"IS_TITLE": True, "OP": "+"}],
        [{"ORTH": "Estate"}, OF, {"ENT_TYPE": Label.PERSON.name}],
    ],
)

ENT_GENERIC_ORG = Rule(
    id="incorporated",
    label=Label.ORG,
    patterns=[
        [
            {"IS_TITLE": True, "OP": "+"},
            {"ORTH": ",", "IS_PUNCT": True, "OP": "?"},
            {
                "LOWER": {"IN": list(set(o.lower() for o in org_options))},
                "IS_TITLE": True,
            },
        ]
    ],
)

ENT_GENERIC_LAWS = Rule(
    id="named-generic-laws",
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
    ],
)

ENT_GENERIC_DOC = Rule(
    id="papers",
    label=Label.Document,
    patterns=[
        [
            {
                "ORTH": {
                    "IN": [
                        "prohibited",
                        "penalty",
                        "dragnet",
                        "liability",
                        "limitation",
                        "loss",
                        "payable",
                        "limited",
                        "double",
                        "insurance",
                        "incontestability",
                        "penal",
                    ]
                },
                "OP": "+",
            },
            {"LEMMA": "clause"},
        ],
        [
            {
                "LOWER": {"IN": ["marriage", "birth", "death", "medical"]},
                "IS_TITLE": False,
            },
            {"LEMMA": "certificate", "IS_TITLE": False},
        ],
        [
            {
                "LOWER": {"IN": ["transfer", "original", "torrens", "duplicate"]},
                "IS_TITLE": False,
            },
            {"LEMMA": "certificate", "IS_TITLE": False},
            {"LOWER": "of", "IS_TITLE": False},
            {"LEMMA": "title", "IS_TITLE": False},
        ],
        [
            {"LOWER": {"IN": ["irregular", "bank", "insured"]}},
            {"LOWER": "deposits"},
        ],
        [
            {"LOWER": {"IN": ["contract", "deed"]}},
            {"LOWER": {"IN": ["of", "to"]}},
            {"LOWER": {"IN": ["absolute", "conditional"]}, "OP": "?"},
            {"LOWER": {"IN": ["sale", "sell", "loan"]}},
        ],
        [{"LOWER": {"IN": ["judicial", "extrajudicial"]}}, {"LOWER": "demand"}],
        [{"LOWER": "demand"}, {"LEMMA": "letter"}],
        [{"LOWER": "position"}, {"LEMMA": "paper"}],
        [
            {"LOWER": {"IN": ["special", "general"]}},
            {"LOWER": "power"},
            {"LOWER": "of"},
            {"LOWER": "attorney"},
        ],
        [{"LOWER": {"IN": ["forged", "falsified"]}}, {"LEMMA": "document"}],
        [
            {
                "LOWER": {
                    "IN": ["lease", "management", "leasehold", "international", "loan"]
                }
            },
            {"LEMMA": {"IN": ["contract", "agreement"]}},
        ],
        [
            {
                "IS_TITLE": True,
                "OP": "{1,3}",
                "ORTH": {"NOT_IN": ["This", "The", "A", "An"]},
            },
            _orth_in(["Writ", "Motion", "Notice", "Contract", "Agreement"]),
            {"ORTH": {"IN": ["of", "to", "for"]}},
            {"IS_TITLE": True, "OP": "+"},
            {"ORTH": {"IN": ["of", "as", "to"]}, "OP": "*"},
            {"IS_TITLE": True, "OP": "+"},
        ],
        [
            {
                "IS_TITLE": True,
                "OP": "{1,3}",
                "ORTH": {"NOT_IN": ["This", "The", "A", "An"]},
            },
            _orth_in(["Writ", "Motion", "Notice", "Contract", "Agreement"]),
            {"ORTH": {"IN": ["of", "to", "for"]}},
            {"IS_TITLE": True, "OP": "+"},
        ],
        [
            {
                "LOWER": {
                    "IN": [
                        "amended",
                        "supplemental",
                        "original",
                        "initiatory",
                        "responsive",
                    ]
                }
            },
            {"LEMMA": "pleading"},
        ],
        [
            {"LOWER": {"IN": ["transfer", "original"]}, "IS_TITLE": True},
            {"LOWER": {"IN": ["certificate", "certificates"]}, "IS_TITLE": True},
            {"LOWER": "of"},
            {"LOWER": "title", "IS_TITLE": True},
            {"LOWER": {"IN": ["no.", "nos."]}, "IS_TITLE": True},
            {"POS": {"IN": ["NUM", "PUNCT", "SYM", "CCONJ", "PROPN"]}, "OP": "*"},
        ],
        [
            {
                "LOWER": {"IN": ["oct", "tct"]},
                "IS_UPPER": True,
            },
            {
                "LOWER": {"IN": ["no.", "nos."]},
                "IS_TITLE": True,
            },
            {"POS": {"IN": ["NUM", "PUNCT", "SYM", "CCONJ", "PROPN"]}, "OP": "*"},
        ],
    ],
)
