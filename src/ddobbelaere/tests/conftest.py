"""
Test configuration.
"""

import pytest

from ddobbelaere.voynich import Manuscript


@pytest.fixture
def manuscript() -> Manuscript:
    """
    Manuscript fixture.
    """
    return Manuscript()
