def is_isogram(string: str) -> bool:
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
