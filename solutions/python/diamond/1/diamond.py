def rows(letter: str) -> list[str]:
    """Creates a diamond corresponding to the given letter of the alphabet

    :param letter: str - a letter of the alphabet to make a diamond for
    :return: list[str] - the diamond created as a list
    """
    midpoint = ord(letter) - ord("A")
    width = midpoint * 2 + 1
    diamond: list[str] = []

    for i in range(midpoint + 1):
        char = chr(ord("A") + i)

        if i == 0:
            line = char.center(width)
        else:
            line = (char + " " * (i * 2 - 1) + char).center(width)

        diamond.append(line)

    diamond += diamond[-2::-1]

    return diamond
