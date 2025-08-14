def rotate(text: str, key: int) -> str:
    """Rotates the given text based on the number given as the key

    :param text: str - the string to rotate
    :param key: int - the amount to rotate the string by
    :return: str - the rotated string
    """
    if key == 0 or key == 26:
        return text

    rotated = ""

    for char in text:
        if char.isupper():
            rotated += chr((ord(char) - ord("A") + key) % 26 + ord("A"))
        elif char.islower():
            rotated += chr((ord(char) - ord("a") + key) % 26 + ord("a"))
        else:
            rotated += char

    return rotated
