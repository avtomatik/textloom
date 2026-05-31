from .mappings import CYRILLIC_TO_LATIN


def transliterate(text: str) -> str:
    """
    Transliterate Russian Cyrillic text to Latin.

    Example:
        Привет -> Privet
    """
    result = []

    for char in text:
        mapped = CYRILLIC_TO_LATIN.get(char.lower())

        if mapped is None:
            result.append(char)
            continue

        if char.isupper():
            mapped = mapped[0].upper() + mapped[1:]

        result.append(mapped)

    return "".join(result)
