import re


def extract_year(morpokh_year: str) -> int:
    """
    This extracts the actual year from a yearstring

    >>> extract_year("year 450 in the 3rd month")
    450

    >>> extract_year("year -450 in the 3rd month")
    -450

    >>> extract_year("year 0 in the 3rd month")
    0

    >>> extract_year("murks")
    Traceback (most recent call last):
      ...
    ValueError: Cannot extract year
    """
    if match := re.search(r"(?P<year>-?\d+)", morpokh_year):
        return int(match.group("year"))

    raise ValueError("Cannot extract year")
