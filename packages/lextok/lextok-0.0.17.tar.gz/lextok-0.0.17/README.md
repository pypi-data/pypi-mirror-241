# lextok

![Github CI](https://github.com/justmars/lextok/actions/workflows/main.yml/badge.svg)

Rule-based tokenizer and pattern matching for basic Philippine entities using spacy.

> [!IMPORTANT]
> Should be used in tandem with [doclex](https://github.com/justmars/doclex)

## Quickstart

```sh
poetry env use 3.11.6 # 3.12 not yet supported
poetry install
poetry shell
python -m spacy download en_core_web_sm # base model
```

## Rationale

### Before

```py
import spacy

nlp = spacy.load("en_core_web_sm")  # no modifications to the model
doc1 = nlp("Sec. 36(b)(21)")
for token in doc1:
    print(f"{token.text=} {token.pos_=} {token.ent_type_=}, {token.i=}")
"""
token.text='Sec' token.pos_='PROPN' token.ent_type_='ORG' token.i=0
token.text='.' token.pos_='PUNCT' token.ent_type_='' token.i=1
token.text='36(b)(21' token.pos_='NUM' token.ent_type_='CARDINAL' token.i=2
token.text=')' token.pos_='PUNCT' token.ent_type_='' token.i=3
"""
```

### After

```py
from lextok import lextok

lex = lextok()  # inclusion of custom tokenizer, attribute and entity ruler
doc2 = lex("Sec. 36(b)(21)")
for token in doc2:
    print(f"{token.text=} {token.pos_=} {token.ent_type_=} {token.i=}")
"""
token.text='Sec.' token.pos_='NOUN' token.ent_type_='ProvisionNum' token.i=0
token.text='36(b)(21)' token.pos_='NUM' token.ent_type_='ProvisionNum' token.i=1
"""
```

Token entities can be merged:

```py
from lextok import lextok

lex = lextok(finalize_entities=True)
doc2 = lex("Sec. 36(b)(21)")
for token in doc2:
    print(f"{token.text=} {token.pos_=} {token.ent_type_=} {token.i=}")
"""
token.text='Sec. 36(b)(21)' token.pos_='NUM' token.ent_type_='ProvisionNum' token.i=0
"""
```

## Pattern creation

A pattern consists of a list of tokens, e.g. space space between the word, a dot, and the number?

```py
[
    {"ORTH": {"IN": ["Tit", "Bk", "Ch", "Sub-Chap", "Art", "Sec", "Par", "Sub-Par"]}},
    {"ORTH": "."},  # with dot
    {"POS": "NUM"},
]
```

This is another pattern where the dot is connected to the word:

```py
[
    {
        "ORTH": {
            "IN": [
                "Tit.",
                "Bk.",
                "Ch.",
                "Sub-Chap.",
                "Art.",
                "Sec.",
                "Par.",
                "Sub-Par.",
            ]
        }
    },
    {"POS": "NUM"},
]  # no separate dot
```

There are many variations. It becomes possible to generate a list of patterns algorithmically and save them to a `*.jsonl` file, e.g.:

```py
from lextok import ENT_PROVISION_NUM

print(ENT_PROVISION_NUM.patterns)  # view patterns
ENT_PROVISION_NUM.create_file()  # located in /lextok/rules/ if path not specified
```

## Detected combinations

### doc._.statutory_provisions

```py
txt0 = "Sec. 36(b)(21), RA 12452"
doc = lex(txt0)
for token in doc:  # reveals 2 entities
    print(f"{token.text=} {token.pos_=} {token.ent_type_=} {token.i=}")
"""
token.text='Sec. 36(b)(21)' token.pos_='NUM' token.ent_type_='ProvisionNum' token.i=0
token.text=',' token.pos_='PUNCT' token.ent_type_='' token.i=1
token.text='RA 12452' token.pos_='PROPN' token.ent_type_='StatuteNum' token.i=2
"""
```

These entities, because of the `Provision` + `Statute` span ruler pattern can be detected with:

```py
doc._.statutory_provisions  # [Sec. 36(b)(21), RA 12452] a single Sapn object
```

The reverse pattern (e.g. `Statute` + `Provision`) is likewise detected:

```py
txt1 = "Republic Act No. 141, Sec. 1"
doc = lex(txt1)
for token in doc:  # reveals 2 entities
    print(f"{token.text=} {token.pos_=} {token.ent_type_=} {token.i=}")
"""
token.text='Republic Act No. 141' token.pos_='PROPN' token.ent_type_='StatuteNum' token.i=0
token.text=', Sec. 1' token.pos_='NOUN' token.ent_type_='ProvisionNum' token.i=1
"""
doc._.statutory_provisions  # ['Republic Act No. 141, Sec. 1']
```

### doc._.decision_citations

```py
txt1 = "A v. B, G.R. Nos. 12414, 6546546, 324235 feb 1, 2021, 50 SCRA 510"
doc = lex(txt1)
for token in doc:  # reveals 2 entities
    print(f"{token.text=} {token.pos_=} {token.ent_type_=} {token.i=}")
"""
token.text='A v. B,' token.pos_='PROPN' token.ent_type_='CaseName' token.i=0
token.text='G.R. Nos. 12414' token.pos_='PROPN' token.ent_type_='DocketNum' token.i=1
token.text=',' token.pos_='PUNCT' token.ent_type_='' token.i=2
token.text='6546546' token.pos_='NUM' token.ent_type_='DATE' token.i=3
token.text=',' token.pos_='PUNCT' token.ent_type_='' token.i=4
token.text='324235' token.pos_='NUM' token.ent_type_='' token.i=5
token.text='feb 1, 2021' token.pos_='PROPN' token.ent_type_='DATE' token.i=6
token.text=',' token.pos_='PUNCT' token.ent_type_='' token.i=7
token.text='50 SCRA 510' token.pos_='PROPN' token.ent_type_='ReporterNum' token.i=8
"""
doc._.decision_citations
"""
['A v. B, G.R. Nos. 12414, 6546546, 324235 feb 1, 2021, 50 SCRA 510']
"""
```

### doc._.statutory_links

```py
link_text = "These are related: Rep. Act No. 123, RA 12452, and RA No. 4543"
doc = lex(link_text)
doc._.statutory_links  # [Rep. Act No. 123, RA 12452, and RA No. 4543]
```

## Customization

### Existing data structures

```py
from lextok import Label, ENTITY_RULES, SPAN_RULES

for label in Label:
    print(label.name)
for e in ENTITY_RULES:
    print(e)
for s in SPAN_RULES:
    print(s)
```

### Add more entity rules

Create a list of `Rule` objects, e.g.:

```py
from lextok import lextok, Rule, ENTITY_RULES, Label

added_rules = [
    Rule(
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
    ),
    Rule(
        id="intermediate-scrutiny",
        label=Label.Doctrine,
        patterns=[
            [
                {"LOWER": "test", "OP": "?"},
                {"LOWER": "of", "OP": "?"},
                {"LOWER": "intermediate"},
                {"LOWER": "scrutiny"},
                {"LEMMA": {"IN": ["test", "approach"]}, "OP": "?"},
            ]
        ],
    ),
]

# Include new rules in lextok language
nlp = lextok(finalize_entities=True, entity_rules=ENTITY_RULES + added_rules)

# Test detection
doc = nlp(
    "Lorem ipsum, sample text. The Ministry of Labor is a govt division. Hello world. The test of intermediate scrutiny is a constitutional law concept."
)
doc.ents  # (The Ministry of Labor, test of intermediate scrutiny)
```

### Add more span rules

Each span ruler is identified by a span key and each key should be _unique_. The basic span keys are derived from each `Rule`'s label, e.g. `StatutoryProvision`. To add more rules to this span key, modify the patterns field, likeso:

```py
from lextok.rules import SPAN_STAT

SPAN_STAT.patterns = SPAN_STAT.patterns + new_pattern
SPANS = [SPAN_STAT]
```
