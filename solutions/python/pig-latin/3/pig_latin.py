VOWELS = {"a", "e", "i", "o", "u"}
VOWELS_Y = {"a", "e", "i", "o", "u", "y"}
SPECIALS = {"xr", "yt"}


def translate(text: str) -> str:
    """Translates English text into Pig Latin

    :param text: str - text to translate
    :return: str - translated text

    Function that takes in a string to be translated and returns the translated
    text based on set rules. (Sets and Slices method)
    """
    translated = []

    for word in text.split():
        if word[0] in VOWELS or word[0:2] in SPECIALS:
            translated.append(word + "ay")
            continue

        for i in range(1, len(word)):
            if word[i] in VOWELS_Y:
                i += 1 if word[i] == "u" and word[i - 1] == "q" else 0
                translated.append(word[i:] + word[:i] + "ay")
                break

    return " ".join(translated)
