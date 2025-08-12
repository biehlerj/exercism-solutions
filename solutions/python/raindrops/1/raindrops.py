def convert(number: int) -> str:
    """Converts a number into it's corresponding rain sound

    :param number: int - The number convert
    :return: str - The rain sound that corresponds to the provided number

    Function that takes in an integer and returns a string that corresponds
    to the given integer.
    """
    sound = ""

    if number % 3 == 0:
        sound += "Pling"
    if number % 5 == 0:
        sound += "Plang"
    if number % 7 == 0:
        sound += "Plong"

    return sound if len(sound) > 0 else str(number)
