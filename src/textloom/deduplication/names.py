from collections import defaultdict
from typing import DefaultDict, Iterable, List


def deduplicate_names(
    values: Iterable[str],
    separator: str = "_",
) -> List[str]:
    """
    Make names unique while preserving order.

    Example:
        ["a", "a", "a"] ->
        ["a", "a_2", "a_3"]
    """

    counts: DefaultDict[str, int] = defaultdict(int)
    result = []

    for value in values:
        counts[value] += 1

        if counts[value] == 1:
            result.append(value)
        else:
            result.append(f"{value}{separator}{counts[value]}")

    return result
