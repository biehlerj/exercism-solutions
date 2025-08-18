def recite(start: int, take: int = 1):
    """Recites the children's song Ten Green Bottles from a given start point
    and repeats it a given number of times

    :param start: int - number of bottles to start with
    :param take: int - number of times to recite the verse
    :return: list[str] - list of the verses
    """
    number_words = {
        0: "no",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
    }
    verses: list[str] = []

    for i in range(start, start - take, -1):
        if i == 1:
            current = "one green bottle"
        else:
            current = f"{number_words[i]} green bottles"
        if i - 1 == 0:
            next_bottles = "no green bottles"
        elif i - 1 == 1:
            next_bottles = "one green bottle"
        else:
            next_bottles = f"{number_words[i - 1]} green bottles"

        verses.append(f"{current.capitalize()} hanging on the wall,")
        verses.append(f"{current.capitalize()} hanging on the wall,")
        verses.append("And if one green bottle should accidentally fall,")
        verses.append(f"There'll be {next_bottles} hanging on the wall.")

        if i != start - take + 1:
            verses.append("")

    return verses
