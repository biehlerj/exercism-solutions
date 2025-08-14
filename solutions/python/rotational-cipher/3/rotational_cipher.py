ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def rotate(text: str, key: int) -> str:
    """Rotates the given text based on the number given as the key

    :param text: str - the string to rotate
    :param key: int - the amount to rotate the string by
    :return: str - the rotated string

    This version uses the alphabet method
    """
    rotated = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                rotated += ALPHABET[(ALPHABET.index(char.lower()) + key) % 26].upper()
            else:
                rotated += ALPHABET[(ALPHABET.index(char) + key) % 26]
        else:
            rotated += char

    return rotated
