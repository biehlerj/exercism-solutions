def convert(number: int) -> str:
    """Converts a number into it's corresponding rain sound

    :param number: int - The number convert
    :return: str - The rain sound that corresponds to the provided number

    Function that takes in an integer and returns a string that corresponds
    to the given integer.
    """
    sounds = {3: "Pling", 5: "Plang", 7: "Plong"}
    compiled_sound = (
        sound for divisor, sound in sounds.items() if number % divisor == 0
    )

    return "".join(compiled_sound) or str(number)
