"""Tests functions in utils program."""
from exercises.ex05.utils import only_evens, sub, concat
author = "730565579"


def test_only_evens_with_big_list() -> None:
    """Use Case: Tests if the function only_evens returns an only even list."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert only_evens(xs) == [2, 4, 6, 8]


def test_only_evens_with_same_number() -> None:
    """Use Case: Tests if the function returns an empty list if given a list of odd numbers."""
    xs: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(xs) == []


def test_only_evens_with_empty_list() -> None:
    """Edge case: tests if the function returns an empty list if given an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_concat_with_two_lists_of_differing_length_and_ints() -> None:
    """Use case: Tests if the concat function returns a list concatonated with another list."""
    list1: list[int] = [1, 2, 3, 4, 5]
    list2: list[int] = [6, 7, 8, 9]
    assert concat(list1, list2) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_concat_with_identical_lists() -> None:
    """Use Case: tests if identical lists get concatonated with each other."""
    list1: list[int] = [6, 7, 8, 9]
    list2: list[int] = [6, 7, 8, 9]
    assert concat(list1, list2) == [6, 7, 8, 9, 6, 7, 8, 9]


def test_concat_with_empty_list() -> None:
    """Edge case: tests if the new list equals the first list when concatonated with an empty list."""
    list1: list[int] = [6, 7, 8, 9]
    list2: list[int] = []
    assert concat(list1, list2) == [6, 7, 8, 9]


def test_start_greater_than_length_of_list() -> None:
    """Edge case: Tests if the function returns an empty list based on the start value being greater than the length of the list."""
    xs: list[int] = [1, 2, 3, 4]
    assert sub(xs, 5, 5) == []


def test_sub_list_big_list() -> None:
    """Use case: tests if function produces range of list based on start and stop values."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert sub(xs, 2, 8) == [3, 4, 5, 6, 7, 8]


def test_sub_list_small_list() -> None:
    """Use case: tests if function produces range with small list."""
    xs: list[int] = [1, 2]
    assert sub(xs, 0, 1) == [1]