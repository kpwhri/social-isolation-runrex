"""
Social isolation as defined by Zhu et al (2019).
"""
from runrex.algo import Pattern
from runrex.algo.result import Status
from runrex.terms import negation, hypothetical
from runrex.text import Document


class IsolationStatus(Status):
    NONE = -1
    ISOLATED = 1
    LONELY = 2
    LACK_SUPPORT = 3
    NOT_ISOLATED = 11
    NOT_LONELY = 12
    NOT_LACK_SUPPORT = 13


social = r'(?:social(?:ly)?|family|friends?)'
isolation = r'(?:isolat\w+|withdrawn?)'
feel = r'feel(?:s|ings?)?(?: of)?'
support = r'(?:support|network|connection)s?'
lack = r'(?:lack|loss|missing|without|limitt?ed)(?: (?:of|any|in))?'

ISOLATED_PAT = Pattern(
    rf'(?:'
    rf'{social} {isolation}'
    rf'|{feel} {isolation}'
    rf')',
    negates=[negation, hypothetical],
)

LONELY_PAT = Pattern(
    rf'(?:'
    rf'lonel(?:y|iness|ier)'
    rf')',
    negates=[negation, hypothetical],
)

NO_SUPPORT_PAT = Pattern(
    rf'(?:'
    rf'not? (?:{social} ){support}'
    rf'|not? {social}'
    rf'|{support} no(?:ne)?'
    rf'|{social} no(?:ne)?'
    rf')',
    negates=[hypothetical],
)

LACK_SUPPORT_PAT = Pattern(
    rf'(?:'
    rf'{lack} (?:{social} )?{support}'
    rf'|{lack} {social}'
    rf')',
    negates=[negation, hypothetical]
)


def has_social_isolation(document: Document):
    for sentence in document:
        for text, start, end, is_neg in sentence.get_patterns(ISOLATED_PAT, return_negation=True):
            if is_neg:
                yield IsolationStatus.NOT_ISOLATED, text, start, end
            else:
                yield IsolationStatus.ISOLATED, text, start, end
        for text, start, end, is_neg in sentence.get_patterns(NO_SUPPORT_PAT, LACK_SUPPORT_PAT, return_negation=True):
            if is_neg:
                yield IsolationStatus.NOT_LACK_SUPPORT, text, start, end
            else:
                yield IsolationStatus.LACK_SUPPORT, text, start, end
        for text, start, end, is_neg in sentence.get_patterns(LONELY_PAT, return_negation=True):
            if is_neg:
                yield IsolationStatus.NOT_LONELY, text, start, end
            else:
                yield IsolationStatus.LONELY, text, start, end
