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
TOLERANCES = {
    "grey": "±0.05%",
    "violet": "±0.1%",
    "blue": "±0.25%",
    "green": "±0.5%",
    "brown": "±1%",
    "red": "±2%",
    "gold": "±5%",
    "silver": "±10%",
}


def resistor_label(colors: list[str]):
    """Creates a label for a resistor

    :param colors: list[str] - colors of the bands on the resistor
    :return: str - created label based on the colors of the bands on the resistor
    """
    match len(colors):
        case 1:
            return "0 ohms"
        case 4:
            d1 = COLORS[colors[0]]
            d2 = COLORS[colors[1]]
            multiplier = COLORS[colors[2]]
            value = (d1 * 10 + d2) * (10**multiplier)
            tolerance = TOLERANCES[colors[3]]
        case 5:
            d1 = COLORS[colors[0]]
            d2 = COLORS[colors[1]]
            d3 = COLORS[colors[2]]
            multiplier = COLORS[colors[3]]
            value = (d1 * 100 + d2 * 10 + d3) * (10**multiplier)
            tolerance = TOLERANCES[colors[4]]
        case _:
            raise ValueError("Invalid number of color bands")

    if value >= 1_000_000_000:
        amount = value / 1_000_000_000
        unit = "gigaohms"
    elif value >= 1_000_000:
        amount = value / 1_000_000
        unit = "megaohms"
    elif value >= 1_000:
        amount = value / 1_000
        unit = "kiloohms"
    else:
        amount = value
        unit = "ohms"

    # Format amount: show up to 2 decimals if needed, else as int
    if isinstance(amount, float) and not amount.is_integer():
        amount_str = f"{amount:.2f}".rstrip("0").rstrip(".")
    else:
        amount_str = str(int(amount))

    return f"{amount_str} {unit} {tolerance}"
