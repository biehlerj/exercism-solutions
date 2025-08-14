def is_valid(isbn: str) -> bool:
    """Checks if a given string is valid ISBN-10

    :param isbn: str - the string to check
    :return: bool - True if the given string is valid ISBN-10 otherwise False
    """
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False

    total = 0

    for i, char in enumerate(isbn):
        if i == 9 and char == "X":
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
            return False

        total += value * (10 - i)

    return total % 11 == 0
