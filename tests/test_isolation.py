import pytest
from runrex.pytest_utils import pytest_algo_function

from social_isolation.algo.isolation import IsolationStatus, has_social_isolation, LACK_SUPPORT_PAT


@pytest.mark.parametrize('text, exp', [
    ('limited social network', True),
])
def test_lack_support_pat(text, exp):
    assert bool(LACK_SUPPORT_PAT.matches(text)) is exp


@pytest.mark.parametrize('text, exp', [
    ('lonely', IsolationStatus.LONELY),
    ('loneliness', IsolationStatus.LONELY),
    ('no friends', IsolationStatus.LACK_SUPPORT),
    ('limited social support', IsolationStatus.LACK_SUPPORT),
    ('lack in social support', IsolationStatus.LACK_SUPPORT),
    ('limited social network', IsolationStatus.LACK_SUPPORT),
    ('lack of social connections', IsolationStatus.LACK_SUPPORT),
    ('has friends', None),
    ('socially isolated', IsolationStatus.ISOLATED),
    ('social isolation', IsolationStatus.ISOLATED),
    ('not socially isolated', IsolationStatus.NOT_ISOLATED),
    ('socially isolated: no', IsolationStatus.NOT_ISOLATED),
    ('feels isolated', IsolationStatus.ISOLATED),
    ('feelings of isolation', IsolationStatus.ISOLATED),
])
def test_has_social_isolation(text, exp):
    assert exp in pytest_algo_function(has_social_isolation, text)
