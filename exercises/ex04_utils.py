"""A simple introduction exercise to lists."""
author: str = "730565579"


def all(input: list[int], main_int: int) -> bool:
    """Returns a bool indicating whether or not all the ints in the list are the same as the given int."""
    index: int = 0
    if len(input) == 0:
        return False
    if len(input) == -1:
        return False
    while index <= len(input) - 1:
        if input[index] == main_int:
            index += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Returns the largest value in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 1
    max_num: int = input[0]
    while index <= len(input) - 1:
        if max_num < input[index]:
            max_num = input[index]
        index += 1
    return max_num


def is_equal(listA: list[int], listB: list[int]) -> bool:
    """Return True if every element at every index is equal in both lists."""
    if listA == [] and listB == []:
        return True
    if len(listA) != len(listB):
        return False
    index: int = 0
    while index <= len(listA) - 1:
        if listA[index] != listB[index]:
            return False
        index += 1
        return True
    return False