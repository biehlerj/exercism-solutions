def find(search_list: list[int], value: int, offset: int = 0):
    """Binary Search function that takes in a list of integers and search for
    the given value. It does this by continuously splitting the list in half.

    :param search_list: list[int] - the list to search through
    :param value: int - the value to find in the list
    :param offset: int - offset for the index to start from in the sublist
    :return: int - the index of the value found
    :raises: ValueError if the provided value is not in the list
    """
    if not search_list:
        raise ValueError("value not in array")

    midpoint = len(search_list) // 2

    if search_list[midpoint] == value:
        return midpoint + offset
    elif search_list[midpoint] < value:
        return find(search_list[midpoint + 1 :], value, offset + midpoint + 1)
    else:
        return find(search_list[:midpoint], value, offset)
