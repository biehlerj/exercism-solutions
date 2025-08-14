def is_valid(isbn: str) -> bool:
    """Checks if a given string is valid ISBN-10

    :param isbn: str - the string to check
    :return: bool - True if the given string is valid ISBN-10 otherwise False

    Converts the string to a list then performs math using iterables.
    """
    isbn_list = list(isbn.replace("-", ""))

    if len(isbn_list) != 10:
        return False

    if isbn_list[-1] == "X":
        isbn_list[-1] = "10"

    if not all([char.isdigit() for char in isbn_list]):
        return False

    return sum(int(x) * y for x, y in zip(isbn_list, range(10, 0, -1))) % 11 == 0
