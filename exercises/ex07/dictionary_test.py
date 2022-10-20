"""Dictionary tests."""
__author__ = "730574521"

from dictionary import invert, favorite_color, count
import pytest


def test_empty_dict_invert() -> None:
    """Tests for an empty dict."""
    assert invert({}) == {}


def test_multiple_values_invert() -> None:
    """Tests for a multiple value dict."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_multiple_values_2_invert() -> None:
    """Tests for a multiple value dict (part 2)."""
    assert invert({'7am': 'morning', '4pm': 'afternoon', '11pm': 'night'}) == {'morning': '7am', 'afternoon': '4pm', 'night': '11pm'}


with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_empty_dict_favorite_color() -> None:
    """Tests for an empty dictionary."""
    assert favorite_color({}) == ""


def test_multiple_str_dict_favorite_color() -> None:
    """Tests for a multiple string dictionary."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_multiple_str_dict_favorite_2_color() -> None:
    """Tests for a multiple string dictionary (part 2)."""
    assert favorite_color({"Tess": "orange", "Lulu": "green", "Maggie": "green"}) == "green"


def test_empty_list_count() -> None:
    """Tests for an empty list."""
    assert count([]) == {}


def test_multiple_int_list_count() -> None:
    """Tests for a multiple string list."""
    assert count(["1", "1", "1", "3", "2", "3"]) == {"1": 3, "3": 2, "2": 1}


def test_multiple_str_list_count() -> None:
    """Tests for a multiple string list (part 2)."""
    assert count(["ice cream", "pizza", "pizza", "hotdog", "ice cream", "ice cream"]) == {"ice cream": 3, "pizza": 2, "hotdog": 1}