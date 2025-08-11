def steps(number: int):
    """Calculates the number of steps it takes to get to a given number to get to 1

    :param number: int - The number to find how many steps to get to 1
    :return: int - The number of steps it took to get to 1

    Function that takes a number and returns how many steps it takes to get to 1
    """
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    count = 0

    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
        count += 1

    return count
