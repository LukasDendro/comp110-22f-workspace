"""Unit tests and lists."""
author = "730565579"


def only_evens(input: list[int]) -> list[int]:
    """Returns a list of only even functions."""
    i: int = 0
    even_list: list[int] = list()
    while i < len(input):
        if input[i] % 2 != 0:
            i += 1
        else:
            even_list.append(input[i])
            i += 1
    return even_list 


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Returns one list of values starting from list1 and ending with list2."""
    list3: list[int] = list()
    i: int = 0
    while i < len(list1):
        list3.append(list1[i])
        i += 1 
    i: int = 0
    while i < len(list2):
        list3.append(list2[i])
        i += 1
    return list3 


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Return a list of values from a list between two ints."""
    sub_list: list[int] = list()
    i: int = start 
    if len(xs) == 0 or start >= len(xs) or end == 0:
        return []
    if i < 0:
        i = 0
    if end > len(xs):
        end = len(xs)
    while i < end:
        sub_list.append(xs[i])
        i += 1
    return sub_list