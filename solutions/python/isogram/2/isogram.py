def is_isogram(string: str) -> bool:
    """Checks if a string is an isogram

    :param string: str - the string to check
    :return: bool - True if the string is an isogram otherwise False
    """
    string = string.lower()
    letters_dict = {}

    for letter in string:
        if letter == "-" or letter.isspace():
            continue
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1

    return all(i == 1 for i in letters_dict.values())
