from lextok.rules._pattern import OF, Label, Rule, _orth_in, lower_words

SPAN_REASONABLE_MAN = Rule(
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


SPAN_PERSONALITIES = Rule(
    id="personalities",
    label=Label.Personality,
    patterns=[
        [
            {"LOWER": {"IN": ["trial", "appellate", "regular", "lower", "inferior"]}},
            {"LEMMA": "court"},
        ],
        [
            {"LOWER": {"IN": ["natural-born", "naturalized"]}},
            {"LEMMA": {"IN": ["citizen", "citizenship", "filipino"]}},
        ],
        [
            {"LOWER": {"IN": ["resident", "nonresident", "non-resident"]}},
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
    ],
)


SPAN_TERMS = Rule(
    id="common-terms",
    label=Label.Common,
    patterns=[
        [
            {
                "LOWER": {
                    "IN": [
                        "general",
                        "special",
                        "amendatory",
                        "remedial",
                        "curative",
                        "enabling",
                        # can't use substantive since "substantive law" of the contract also possible; see also arbitration
                        "procedural",
                    ]
                }
            },
            {"LEMMA": {"IN": ["statute", "law", "provision", "legislation"]}},
        ],
        [{"LOWER": {"IN": ["good", "bad"]}}, {"LOWER": "faith"}],
        [{"LOWER": "factual"}, {"LEMMA": {"IN": ["finding", "issue"]}}],
        [
            {"LEMMA": {"IN": ["finding", "issue", "trier"]}},
            {"LOWER": "of"},
            {"LEMMA": "fact"},
        ],
        lower_words("findings of the trial court"),
        lower_words("resolution of the factual issues"),
        lower_words("caso fortuito"),
        lower_words("force majeure"),
        lower_words("act of god"),
        [
            {"LOWER": {"IN": ["ex", "pro"]}},
            {"ORTH": "-", "OP": "?"},
            {"LOWER": {"IN": ["parte", "forma"]}},
            {"LOWER": {"IN": ["motion", "rule"]}},
        ],
        [{"LOWER": {"IN": ["court", "judicial"]}}, {"LEMMA": "record"}],
        [{"LOWER": "case"}, {"LOWER": "at"}, {"LOWER": {"IN": ["bar", "bench"]}}],
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
    ],
)

SPAN_DECISION_PARTS = Rule(
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


SPAN_PAPERS = Rule(
    id="papers",
    label=Label.Paper,
    patterns=[
        [{"LOWER": {"IN": ["insurance", "company"]}}, {"LEMMA": "policy"}],
        [{"LOWER": "promissory"}, {"LEMMA": "note"}],
        [
            {"LOWER": {"IN": ["mere", "useless"]}},
            {"LOWER": {"IN": ["piece", "scrap"]}},
            {"LOWER": "of"},
            {"LOWER": "paper"},
        ],
        [
            {
                "LOWER": {"IN": ["marriage", "birth", "death", "medical"]},
                "IS_TITLE": False,
            },
            {"LEMMA": "certificate", "IS_TITLE": False},
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
    ],
)
