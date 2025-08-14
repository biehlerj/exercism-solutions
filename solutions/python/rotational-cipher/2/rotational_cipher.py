ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def rotate(text: str, key: int) -> str:
    """Rotates the given text based on the number given as the key

    :param text: str - the string to rotate
    :param key: int - the amount to rotate the string by
    :return: str - the rotated string

    This version uses the str.translate method
    """
    translator = ALPHABET[key:] + ALPHABET[:key]

    return text.translate(
        str.maketrans(ALPHABET + ALPHABET.upper(), translator + translator.upper())
    )
