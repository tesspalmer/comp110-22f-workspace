"""Dictionary functions."""
__author__ = "730574521"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary."""
    result: dict[str, str] = {}
    for x in a:
        if a[x] in result:
            raise KeyError("cannot be multiple of the same key.")
        result[a[x]] = x
    return result


def favorite_color(a: dict[str, str]) -> str:
    """Returns the favorite color that appears most frequently in a dict of people's favorite colors."""
    result: str = ""
    max_int: int = 0
    counter: dict[str, int] = {}
    for x in a:
        if a[x] in counter:
            counter[a[x]] += 1
        else:
            counter[a[x]] = 1
    for x in counter:
        if max_int < counter[x]:
            max_int = counter[x]
            result = x
    return result


def count(a: list[str]) -> dict[str, int]:
    """Returns how many times a string appears in a list."""
    result: dict[str, int] = {}
    for x in a:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1
    return result