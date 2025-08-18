COLORS = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def value(colors: list[str]) -> int:
    """Gets the value of the resistor based on the bands

    :param colors: list[str] - colors of the bands to get the value of
    :return: int - the value of the resistor
    """
    value_str = f"{COLORS[colors[0]]}{COLORS[colors[1]]}"

    return int(value_str)
