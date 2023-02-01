from runrex.algo import Pattern
from runrex.algo.result import Status
from runrex.terms import negation, hypothetical
from runrex.text import Document


class IsAloneStatus(Status):
    NONE = -1
    ALONE = 1


IS_ALONE_PAT = Pattern(
    rf'(?:'
    rf'(?:live|reside|dwell)s? (?:alone|by (?:him|her)self)'
    rf')',
    negates=[negation, hypothetical],
)


def is_alone(document: Document):
    for sentence in document:
        for text, start, end in sentence.get_patterns(IS_ALONE_PAT):
            yield IsAloneStatus.ALONE, text, start, end
