def is_pangram(sentence: str):
    """Checks if a given sentence is a pangram

    :param sentence: str - sentence to check
    :return: bool - True if the sentence is a pangram otherwise False

    A sentence is a pangram if it contains all of the 26 letters in the English
    alphabet at least once. The check should be case insensitive
    """
    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    return alphabet <= set(sentence.lower())
