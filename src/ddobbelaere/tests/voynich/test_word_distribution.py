"""
Word distribution tests.
"""

from collections import defaultdict

from ddobbelaere.voynich import Manuscript


def test_word_distribution(manuscript: Manuscript):
    """
    Test word distribution.
    """
    words = manuscript.words

    assert len(words) > 0

    # Calculate distribution.
    count: dict[str, int] = defaultdict(lambda: 0)

    for word in words:
        count[word] += 1

    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)

    print(sorted_count)
