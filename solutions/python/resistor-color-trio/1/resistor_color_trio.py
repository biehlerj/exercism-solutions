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


def label(colors: list[str]):
    """Calculates how many ohms a resistor is based on it's colors

    :param colors: list[str] - the colors of the bands on the resistor
    :return: str - how many ohms the resistor is
    """
    value = COLORS.index(colors[0]) * 10 + COLORS.index(colors[1])
    multiplier = 10 ** COLORS.index(colors[2])
    ohms = value * multiplier

    match ohms:
        case ohm if ohm >= 1_000_000_000:
            amount = ohm // 1_000_000_000
            unit = " gigaohms"
        case ohm if ohm >= 1_000_000:
            amount = ohm // 1_000_000
            unit = " megaohms"
        case ohm if ohm >= 1_000:
            amount = ohm // 1_000
            unit = " kiloohms"
        case _:
            amount = ohms
            unit = " ohms"

    return f"{amount}{unit}"
