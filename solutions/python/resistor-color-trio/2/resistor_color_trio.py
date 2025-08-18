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


def label(colors: list[str]):
    """Calculates how many ohms a resistor is based on it's colors

    :param colors: list[str] - the colors of the bands on the resistor
    :return: str - how many ohms the resistor is
    """
    value = COLORS[colors[0]] * 10 + COLORS[colors[1]]
    multiplier = 10 ** COLORS[colors[2]]
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
