from pathlib import Path

from .identifier import normalize_identifier


def normalize_filename(name: str) -> str:
    """
    Normalize a filename into a filesystem-friendly slug.

    Example:
        "Мой файл.xlsx" -> "moy-fayl.xlsx"
    """
    path = Path(name)

    stem = normalize_identifier(
        path.stem,
        separator="-",
    )

    suffix = "".join(path.suffixes).lower()

    return f"{stem}{suffix}"
