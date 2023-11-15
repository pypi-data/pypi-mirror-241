from ._pattern import (
    CM,
    CODE,
    CONNECTOR,
    COURT,
    OF,
    OF_THE_PH_,
    PROV_DIGITS,
    TH,
    THE,
    VS,
    DigitLists,
    Label,
    Rule,
    _orth_in,
    _re,
    camel_case_pattern,
    lower_words,
    name_code,
    name_court,
    name_statute,
    titled_words,
    uncamel,
)
from .abbreviations import (
    Abbv,
    Prov,
)
from .attribute_ruler import Attr, WordAttributes
from .citeable_builder import Duo, Style
from .custom_tokenizer import (
    INFIXES_OVERRIDE,
    create_special_rules,
    custom_prefix_list,
    custom_suffix_list,
)
from .entity_rules_citeable import (
    ENT_COURT_NAME,
    ENT_DOCKET_NUM,
    ENT_GENERIC_NUM,
    ENT_PROVISION_NUM,
    ENT_REPORTER_NUM,
    ENT_STATUTE_NUM,
    SPAN_DECISION_CITATION,
    SPAN_GENERIC_DOC,
    SPAN_LINKED_STAT,
    SPAN_STAT_PROV,
    CourtName,
    DocketNum,
    ProvisionNum,
    ReporterNum,
    StatuteNum,
)
from .entity_rules_generic import (
    ENT_CASE_NAME,
    ENT_CUSTOM_DATE,
    ENT_GENERIC_COMMON_TERMS,
    ENT_GENERIC_DECISION_PARTS,
    ENT_GENERIC_DOC,
    ENT_GENERIC_ESTATE,
    ENT_GENERIC_LAWS,
    ENT_GENERIC_ORG,
    ENT_GENERIC_PERSON_PREFIX,
    ENT_GENERIC_PERSONALITY,
    ENT_REASONABLE_MAN,
)
from .pretest import pretest_entities

SPAN_RULES = [
    SPAN_GENERIC_DOC,
    SPAN_DECISION_CITATION,
    SPAN_STAT_PROV,
    SPAN_LINKED_STAT,
]
ENTITY_RULES = [
    ENT_CASE_NAME,
    ENT_COURT_NAME,
    ENT_CUSTOM_DATE,
    ENT_PROVISION_NUM,
    ENT_REPORTER_NUM,
    ENT_GENERIC_ORG,
    ENT_GENERIC_DOC,
    ENT_GENERIC_ESTATE,
    ENT_GENERIC_LAWS,
    ENT_GENERIC_PERSON_PREFIX,
    ENT_GENERIC_PERSONALITY,
    ENT_GENERIC_COMMON_TERMS,
    ENT_GENERIC_DECISION_PARTS,
    ENT_REASONABLE_MAN,
    ENT_STATUTE_NUM,
    ENT_DOCKET_NUM,
    ENT_GENERIC_NUM,
]


LABELS_BUILT_IN = [
    Label.PERSON,
    Label.GPE,
    Label.ORG,
    Label.LAW,
]
LABELS_STATUTORY = [
    Label.ProvisionNum,
    Label.StatuteNamed,
    Label.StatuteNum,
]
LABELS_CITATION = [
    Label.CaseName,
    Label.DocketNum,
    Label.ReporterNum,
]
LABELS_GENERIC = [
    Label.GenericNum,
    Label.Personality,
    Label.Document,
]

EXT_ENTS = LABELS_BUILT_IN + LABELS_STATUTORY + LABELS_CITATION + LABELS_GENERIC
"""A collection of _entity-based_ labels that will be extended by the Detector component"""

EXT_SPANS = [
    Label.StatutoryLink,
    Label.DecisionCitation,
    Label.GenericDocument,
    Label.StatutoryProvision,
]
"""A collection of _span-ruler-based_ labels that will be extended by the Detector component"""
