import spacy
from spacy.lang.char_classes import (
    ALPHA,
    ALPHA_LOWER,
    ALPHA_UPPER,
    CONCAT_QUOTES,
    LIST_ELLIPSES,
    LIST_ICONS,
)

from lextok.rules.abbreviations import Abbv, Prov
from lextok.rules.entity_rules_citeable import DocketNum, StatuteNum

# Remove hyphen '-' as infix, see https://spacy.io/usage/linguistic-features#native-tokenizer-additions
INFIXES_OVERRIDE = (
    LIST_ELLIPSES
    + LIST_ICONS
    + [
        r"(?<=[0-9])[+\\-\\*^](?=[0-9-])",
        r"(?<=[{al}{q}])\\.(?=[{au}{q}])".format(
            al=ALPHA_LOWER, au=ALPHA_UPPER, q=CONCAT_QUOTES
        ),
        r"(?<=[{a}]),(?=[{a}])".format(a=ALPHA),
        # ✅ Commented out regex that splits on hyphens between letters:
        # r"(?<=[{a}])(?:{h})(?=[{a}])".format(a=ALPHA, h=HYPHENS),
        r"(?<=[{a}0-9])[:<>=/](?=[{a}])".format(a=ALPHA),
    ]
)


def custom_prefix_list(nlp: spacy.language.Language):
    """Only use prefix `(` and `[` if _not_ followed by a single word `\\w+`
    with a closing `)` or `]`

    Note that modifications to a prefix should be done after the prefix removed, e.g.
    if the prefix is `(`, modify the `(`<add here> when appending a new rule.
    This is because of `compile_suffix_regex` which appends a `^` at the start of every prefix.

    example | status of `(`
    --:|:--
    `(`Juan de la Cruz v. Example) | is prefix
    Juan `(`de) la Cruz v. Example | is _not_ prefix
    """
    pre = list(nlp.Defaults.prefixes)  # type: ignore
    pre.remove("\\(")
    pre.append("\\((?![\\w\\.]+\\))")

    pre.remove("\\[")
    pre.append("\\[(?![\\w\\.]+\\])")
    return pre


def custom_suffix_list(nlp: spacy.language.Language):
    sfx = list(nlp.Defaults.suffixes)  # type: ignore
    sfx.remove("\\)")
    sfx.remove("\\]")
    return sfx


def create_special_rules():
    def make_special(texts: list[str]):
        """Add a period after every text item in `texts`, to consider each a single token.
        These patterns can be used as a special rule in creating a custom tokenizer."""
        return {f"{t}.": [{"ORTH": f"{t}."}] for t in texts if not t.endswith(".")}

    x = make_special("vs v s et al etc Ll Pp PP P.P R.P H.B S.B a.k.a".split())

    a = {
        k: v
        for member in DocketNum
        if member.value.initials
        for k, v in member.value.initials.as_token.items()
    }

    b = {
        k: v
        for member in StatuteNum
        if member.value.initials
        for k, v in member.value.initials.as_token.items()
    }

    c = {
        f"{bit}.": [{"ORTH": f"{bit}."}]
        for style in (None, "lower", "upper")
        for bit in Abbv.set_abbvs(cased=style)
    }

    d = {
        f"{bit}.": [{"ORTH": f"{bit}."}]
        for style in (None, "lower", "upper")
        for bit in Prov.set_abbvs(cased=style)
    }

    return a | b | c | d | x
