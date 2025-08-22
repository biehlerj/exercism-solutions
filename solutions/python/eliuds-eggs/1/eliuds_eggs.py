def egg_count(display_value: int):
    """Counts the number of eggs in the coop and returns the value of actual eggs

    :param display_value: int - the value of the display
    :return: int - the number of actual eggs in the coop based on the decoded binary
    """
    count = 0
    n = display_value

    while n:
        count += n & 1
        n >>= 1

    return count
