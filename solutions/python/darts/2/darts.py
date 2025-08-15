from math import ceil, hypot
from typing import Literal


def score(x: int, y: int) -> Literal[10] | Literal[5] | Literal[1] | Literal[0]:
    """Calculates the score of a toss in a game of Darts based on the x,y coordinates

    :param x: int - location of the dart on the x axis
    :param y: int - location of the dart on the y axis
    :return: int - score of the toss based on it's location

    v2 uses the builtin `match/case` available only on Python v3.10+
    """
    match ceil(hypot(x, y)):
        case 0 | 1:
            return 10
        case 2 | 3 | 4 | 5:
            return 5
        case 6 | 7 | 8 | 9 | 10:
            return 1
        case _:
            return 0
