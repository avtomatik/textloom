import re
import unicodedata

from ..transliteration.core import transliterate


def normalize_text(
    text: str,
    *,
    lowercase: bool = True,
    transliterate_cyrillic: bool = True,
    collapse_whitespace: bool = True,
) -> str:
    text = unicodedata.normalize("NFKC", str(text))

    if transliterate_cyrillic:
        text = transliterate(text)

    if lowercase:
        text = text.lower()

    if collapse_whitespace:
        text = re.sub(r"\s+", " ", text).strip()

    return text
