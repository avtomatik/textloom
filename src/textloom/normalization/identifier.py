import re
import unicodedata

from ..transliteration.core import transliterate


def normalize_identifier(
    value: str,
    *,
    separator: str = "_",
    lowercase: bool = True,
    transliterate_cyrillic: bool = True,
    ascii_only: bool = True,
    collapse_separators: bool = True,
    strip_separators: bool = True,
) -> str:
    """
    Normalize arbitrary text into a clean identifier.

    Examples:
        "Цена товара" -> "cena_tovara"
        "Revenue ($)" -> "revenue"
    """

    text = unicodedata.normalize("NFKC", str(value))

    if transliterate_cyrillic:
        text = transliterate(text)

    if lowercase:
        text = text.lower()

    if ascii_only:
        pattern = r"[^a-z0-9]+"
    else:
        pattern = r"\W+"

    text = re.sub(pattern, separator, text)

    if collapse_separators:
        text = re.sub(
            rf"{re.escape(separator)}+",
            separator,
            text,
        )

    if strip_separators:
        text = text.strip(separator)

    return text
