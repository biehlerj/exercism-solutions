def egg_count(display_value: int):
    """Counts the number of eggs in the coop and returns the value of actual eggs

    :param display_value: int - the value of the display
    :return: int - the number of actual eggs in the coop based on the decoded binary
    """
    count = 0

    while display_value:
        count += display_value & 1
        display_value >>= 1

    return count
