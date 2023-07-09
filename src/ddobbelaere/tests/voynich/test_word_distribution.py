"""
Word distribution tests.
"""

from collections import defaultdict
from typing import Final

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

    print(f"Found {len(set(words))} unique words out of {len(words)} total words")
    print()

    column_width: Final = 10
    max_num_examples: Final = 20
    print(
        f"{'#times':<{column_width}}{'#words':<{column_width}}{'words':<{column_width}}"
    )
    print("-" * 3 * column_width)
    for num_times in range(sorted_count[0][1], 0, -1):
        # pylint:disable=cell-var-from-loop
        filtered_words = list(filter(lambda x: x[1] == num_times, sorted_count))
        num_words = len(filtered_words)

        if num_words > 0:
            example_words = ", ".join(
                list(
                    map(
                        lambda x: x[0],
                        filtered_words[: min(max_num_examples, num_words)],
                    )
                )
            )
            if num_words > max_num_examples:
                example_words += "..."

            print(
                f"{num_times:<{column_width}}{num_words:<{column_width}}{example_words:<{column_width}}"
            )
