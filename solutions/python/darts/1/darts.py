import math
from typing import Literal


def score(x: int, y: int) -> Literal[10] | Literal[5] | Literal[1] | Literal[0]:
    """Calculates the score of a toss in a game of Darts based on the x,y coordinates

    :param x: int - location of the dart on the x axis
    :param y: int - location of the dart on the y axis
    :return: int - score of the toss based on it's location
    """
    distance = math.hypot(x, y)

    if distance <= 1:
        return 10
    if distance <= 5:
        return 5
    if distance <= 10:
        return 1
    return 0
