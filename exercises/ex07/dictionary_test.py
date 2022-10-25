"""Tests functions in dictionary program."""
from exercises.ex07.dictionary import invert, favorite_color, count
import pytest
__author__ = "730565579"


def test_invert_many_keys_values() -> None:
    """Use case that tests if the invert function inverts a dictionary of many values."""
    xs: dict[str, str] = {'tom': 'brady', 'aaron': 'rodgers', 'russel': 'wilson', 'patrick': 'mahomes', 'jared': 'goff'}
    assert invert(xs) == {'brady': 'tom', 'rodgers': 'aaron', 'wilson': 'russel', 'mahomes': 'patrick', 'goff': 'jared'}


def test_invert_two_inverted_values() -> None:
    """Use case that tests if the invert function inverts an already inverted indice."""
    xs: dict[str, str] = {'tom': 'brady', 'brady': 'tom'}
    assert invert(xs) == {'brady': 'tom', 'tom': 'brady'}


def test_one_value() -> None:
    """Edge case that tests what the function will do if there are identical key values."""
    my_dictionary = {'kris': 'jackson'}
    assert invert(my_dictionary) == {'jackson': 'kris'}


with pytest.raises(KeyError):
    """Edge case that tests if the KeyError is raised if two keys are identical."""
    my_dictionary = {'kris': 'jordan', 'micheal': 'jordan'}
    invert(my_dictionary)


def test_favorite_color_my_favorite_color() -> None:
    """Use case that tests if my favorite color (navy) is selected when it is most frequent."""
    xs: dict[str, str] = {'tom': 'blue', 'riley': 'navy', 'lukas': 'navy', 'cole': 'red'}
    assert favorite_color(xs) == "navy"


def test_favorite_color_every_color() -> None:
    """Use case that tests if the favorite color is the color that shows up first when each color has the same frequency."""
    xs: dict[str, str] = {'tom': 'red', 'riley': 'navy', 'cole': 'blue'}
    assert favorite_color(xs) == "red"


def test_favorite_color_two_frequent_colors() -> None:
    """Edge case that tests if the function produces the color that comes up first in the list when tied."""
    xs: dict[str, str] = {'tom': 'blue', 'riley': 'navy', 'lukas': 'navy', 'cole': 'red', 'sophie': 'blue'}
    assert favorite_color(xs) == "blue"


def test_count_random_list_of_letters() -> None:
    """Use case that sorts out the frequency of a random list of nums."""
    xs: list[str] = ["a", "b", "b", "c", "a", "b", "d"]
    assert count(xs) == {"a": 2, "b": 3, "c": 1, "d": 1}


def test_count_ordered_pair_of_nums() -> None:
    """Use case that tests the frequency of nums counting from 1 to 5."""
    xs: list[str] = [1, 2, 3, 4, 5]
    assert count(xs) == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}


def test_count_same_item() -> None:
    """Edge case that tests the frequency of one letter only."""
    xs: list[str] = ["a", "a", "a", "a", "a"]
    assert count(xs) == {"a": 5}