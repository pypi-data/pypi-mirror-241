import spacy  # type: ignore
from spacy.language import Language
from spacy.tokenizer import Tokenizer  # type: ignore
from spacy.tokens import Doc, Span
from spacy.util import filter_spans

from .rules import (
    ENTITY_RULES,
    EXT_ENTS,
    EXT_SPANS,
    INFIXES_OVERRIDE,
    SPAN_RULES,
    Label,
    Prov,
    Rule,
    WordAttributes,
    create_special_rules,
    custom_prefix_list,
    custom_suffix_list,
)


def set_tokenizer(nlp: Language) -> Tokenizer:
    infix_re = spacy.util.compile_infix_regex(INFIXES_OVERRIDE)  # type: ignore
    suffix_re = spacy.util.compile_suffix_regex(custom_suffix_list(nlp))
    prefix_re = spacy.util.compile_prefix_regex(custom_prefix_list(nlp))
    return Tokenizer(
        nlp.vocab,
        rules=create_special_rules(),
        prefix_search=prefix_re.search,
        suffix_search=suffix_re.search,
        infix_finditer=infix_re.finditer,
    )


def set_attribute_ruler(nlp: Language):
    ruler = nlp.get_pipe("attribute_ruler")
    for rule in WordAttributes.make_attr_rules():
        ruler.add(**rule)  # type: ignore
    for rule in Prov.make_attr_rules():
        ruler.add(**rule)  # type: ignore
    return nlp


def create_custom_entities(
    nlp: Language, rules: list[Rule], pipename: str = "entity_ruler"
):
    ents = nlp.add_pipe(
        factory_name="entity_ruler",
        name=pipename,
        config={"overwrite_ents": True, "validate": True},
        validate=True,
    )
    for rule in rules:
        ents.add_patterns(rule.model_dump())  # type: ignore
    return nlp


def create_custom_spans(nlp: Language, rules: list[Rule]):
    for rule in rules:
        spans = nlp.add_pipe(
            "span_ruler",
            name=f"span{rule.label.name}",
            config={"spans_key": rule.label.name, "validate": True},
            validate=True,
        )
        spans.add_patterns(rule.model_dump())  # type: ignore
    return nlp


@Language.component("provision_num_merger")
def merge_provisions(doc: Doc) -> Doc:
    """Consecutive `ProvisionNum` entities merged as a _single_ `ProvisionNum` token and entity."""
    pairs = [(e.start, e.end) for e in doc.ents if e.label_ == Label.ProvisionNum.name]
    pair = None
    new_ents = []
    for ent in doc.ents:
        if ent.label_ == Label.ProvisionNum.name:
            s = ent.start
            if pair and s == pair[1]:
                s = pair[0]
            pair = (s, ent.end)
        if pair and pair not in pairs:
            new_ents.append(
                Span(doc=doc, start=pair[0], end=pair[1], label=Label.ProvisionNum.name)
            )
    if new_ents:
        doc.ents = filter_spans(new_ents + list(doc.ents))
    return doc


@Language.factory("detector")
class EntitySpanDetectorComponent:
    """Dynamic creation of custom attributes (`doc._.<attribute>`)  based on `Label` objects."""

    def __init__(self, nlp, name):
        for label in EXT_ENTS + EXT_SPANS:
            Doc.set_extension(label.snakecase, default=[])

    def __call__(self, doc):
        for label in EXT_ENTS:
            doc._.set(label.snakecase, label.extract_entities(doc))

        for label in EXT_SPANS:
            doc._.set(label.snakecase, label.extract_spans(doc))
        return doc


def lextok(
    model: str = "en_core_web_sm",
    finalize_entities: bool = False,
    entity_rules: list[Rule] = ENTITY_RULES,
    span_rules: list[Rule] = SPAN_RULES,
) -> Language:
    """Incorporation of:

    1. overrides for `set_tokenizer()` and `set_attribute_ruler()`
    2. extendible `ENTITY_RULES` and `SPAN_RULES` based on `Rule` object
    3. last pipe `detector` which creates custom attributes on each `Doc`
    based on `Label`s detected.

    Args:
        model (str, optional): Spacy language model. Defaults to "en_core_web_sm".
        finalize_entities (bool, optional): Whether to consider consecutive entities as a single token. Defaults to False.
        entity_rules (list[Rule], optional): List of generic Pydantic models with serialization. Defaults to `ENTITY_RULES`.
        span_rules (list[Rule], optional): List of generic Pydantic models with serialization. Defaults to `SPAN_RULES`.

    Returns:
        Language: A customized rule-based spacy model.
    """
    nlp = spacy.load(model)
    nlp.tokenizer = set_tokenizer(nlp)
    nlp = set_attribute_ruler(nlp)
    create_custom_entities(nlp, rules=entity_rules, pipename="entity_ruler")
    if finalize_entities:
        nlp.add_pipe("merge_entities", after="entity_ruler")
        nlp.add_pipe("provision_num_merger", after="merge_entities")
        create_custom_spans(nlp, rules=span_rules)
        nlp.add_pipe("detector", last=True)
    return nlp
