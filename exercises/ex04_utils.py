"""List Utility Functions."""
__author__ = "730574521"

def all(number_list: list[int], single_number: int) -> bool:
    i: int = 0
    while i < len(number_list):
        if number_list[i] == single_number:
            i += 1
        else:
            return False
    return True

def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        current_max: int = input[0]
        i: int = 1
        while i < len(input):
            if current_max < input[i]:
                current_max = input[i]
            i += 1
        return current_max

def is_equal(list_a: list[int], list_b: list[int]) -> bool:
    if len(list_a) != len(list_b):
        return False
    i: int = 0
    while i < len(list_a):
        if list_a[i] != list_b[i]:
            return False
        i += 1
    return True