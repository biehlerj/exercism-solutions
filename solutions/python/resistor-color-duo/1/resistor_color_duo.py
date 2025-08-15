COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def value(colors: list[str]) -> int:
    """Gets the value of the resistor based on the bands

    :param colors: list[str] - colors of the bands to get the value of
    :return: int - the value of the resistor
    """
    value_str = f"{COLORS.index(colors[0])}{COLORS.index(colors[1])}"

    return int(value_str)
