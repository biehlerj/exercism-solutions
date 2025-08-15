def color_code(color: str) -> int:
    """Gets the corresponding number of given color

    :param color: str - color to get the number of
    :return: int - color's number code
    """
    return colors().index(color)


def colors() -> list[str]:
    """Returns all the colors in order

    :return: list[str] - all the colors in order
    """
    return [
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
