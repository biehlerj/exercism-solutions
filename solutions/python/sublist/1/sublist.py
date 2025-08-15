"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
from typing import Literal

SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"


def is_sublist(small: list, big: list) -> bool:
    """Check if 'small' is a contiguous sublist of 'big'.

    :param small: list - the smaller list to compare
    :param big: list - the bigger list to compare
    :return: bool - True if small is a contiguous sublist of big otherwise False
    """
    n, m = len(small), len(big)

    if n == 0:
        return True
    return any(small == big[i : i + n] for i in range(m - n + 1))


def sublist(
    list_one: list, list_two: list
) -> Literal["equal"] | Literal["sublist"] | Literal["superlist"] | Literal["unequal"]:
    """Determines if two lists are equal, is a superlist, or is a sublist.

    :param list_one: list - the first list to compare
    :param list_two: list - the second list to compare
    :return: str - what the lists are to each other
    """
    if list_one == list_two:
        return EQUAL
    if is_sublist(list_one, list_two):
        return SUBLIST
    if is_sublist(list_two, list_one):
        return SUPERLIST
    return UNEQUAL
