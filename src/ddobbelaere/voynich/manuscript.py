"""
Voynich manuscript related functionality.
"""

import re
from pathlib import Path


class Manuscript:
    """
    Voynich manuscript class.
    """

    def __init__(self, transcription: str | None = None):
        self._transcription = (
            transcription
            or open(
                Path(__file__).parent.joinpath("data/transcription.txt"),
                encoding="utf8",
            ).read()
        )

        self._init()

    def _init(self) -> None:
        # Convert transcription to list of words.
        word_pattern: str = r"[a-z*]+"
        tag_pattern: str = r"<.+>"
        self._words = re.findall(
            word_pattern, re.sub(tag_pattern, "", self._transcription)
        )

    @property
    def words(self) -> list[str]:
        """
        @return: the list of words as they appear in the manuscript.
        """
        return self._words
