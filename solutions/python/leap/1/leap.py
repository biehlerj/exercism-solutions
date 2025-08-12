def leap_year(year: int) -> bool:
    """Determines if a given year is a Leap year

    :param year - int: The year to check
    :return: bool - True if leap year otherwise False

    Function that takes in a year as a number and determines if it
    is a Leap year.
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False
