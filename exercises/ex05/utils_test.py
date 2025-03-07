"""Tests for the only_evens, concat, and sub functions."""
__author__: "730574521"


from utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Tests for an empty list."""
    assert only_evens([]) == []


def test_only_evens_multiple_items() -> None:
    """Tests for a multiple item list."""
    assert only_evens([1, 2, 3, 4, 5]) == [2, 4]


def test_only_evens_multiple_items2() -> None:
    """Tests for a multiple item list."""
    assert only_evens([5, 42, 7, 10, 13, 1]) == [42, 10]


def test_concat_empty() -> None:
    """Tests for an empty list."""
    assert concat([], []) == []


def test_concat_multiple_ints() -> None:
    """Tests for a multiple item list."""
    assert concat([1, 8, 3, 4], [10, 12, 16]) == [1, 8, 3, 4, 10, 12, 16]


def test_concat_multiple_ints2() -> None:
    """Tests for a multiple item list."""
    assert concat([-2, -3, 10, 8], [3, 40, -100]) == [-2, -3, 10, 8, 3, 40, -100]


def test_sub_empty_list() -> None:
    """Tests for an empty list."""
    assert sub([], 1, 3) == []


def test_sub_single_int() -> None:
    """Tests for a single item list."""
    assert sub([10, 20, 30], -2, 1) == [10]


def test_sub_multiple_ints() -> None:
    """Tests for a multiple item list."""
    assert sub([13, 19, 20, 2], 2, 8) == [20, 2]