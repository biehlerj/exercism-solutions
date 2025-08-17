def square_root(number: int) -> int:
    """Return the integer square root of a non-negative integer.

    :param number: int - number to find the square root of
    :return: int - square root
    """
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number.")

    x = number
    y = (x + 1) // 2

    while y < x:
        x = y
        y = (x + number // x) // 2

    return x
