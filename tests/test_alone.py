import pytest
from runrex.pytest_utils import pytest_algo_function

from social_isolation.algo.alone import IsAloneStatus, is_alone, IS_ALONE_PAT


@pytest.mark.parametrize('text, exp', [
    ('lives alone', True),
])
def test_lack_support_pat(text, exp):
    assert bool(IS_ALONE_PAT.matches(text)) is exp


@pytest.mark.parametrize('text, exp', [
    ('she lives alone', IsAloneStatus.ALONE),
    ('he resides by himself', IsAloneStatus.ALONE),
    ('lives with dtr', None),
])
def test_has_social_isolation(text, exp):
    assert exp in pytest_algo_function(is_alone, text)
