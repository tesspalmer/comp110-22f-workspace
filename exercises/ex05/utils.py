"""Utils 'list' Utility Functions."""
__author__: "730574521"


def only_evens(input: list[int]) -> int:
    """Returns all of the even integers in a given list."""
    i: int = 0
    x: list = []
    while i < len(input):
        if input[i] % 2 == 0:
            x.append(input[i])
        i += 1
    return x


def concat(list_1: list[int], list_2: list[int]):
    """Given two different lists, returns a combined list of the two."""
    i: int = 0
    x: list = []
    while i < len(list_1):
        x.append(list_1[i])
        i += 1
    e: int = 0
    while e < len(list_2):
        x.append(list_2[e])
        e += 1
    return x


def sub(lst_1: list[int], int_1: int, int_2: int ) -> int:
    """Returns a subset of a given list."""
    x: list = []
    if len(lst_1) == 0:
        return x
    if int_1 > len(lst_1):
        return x
    if int_2 <= 0:
        return x
    if int_1 < 0:
        int_1 = 0
    if int_2 > len(lst_1):
        int_2 = len(lst_1)
    while int_1 < int_2:
        x.append(lst_1[int_1])
        int_1 += 1
    return x