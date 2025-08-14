def is_isogram(string: str) -> bool:
    """Checks if a string is an isogram

    :param string: str - the string to check
    :return: bool - True if the string is an isogram otherwise False

    Uses the scrubbing method with multiple replaces.
    """
    scrubbed = string.replace("-", "").replace(" ", "").lower()

    return len(scrubbed) == len(set(scrubbed))
