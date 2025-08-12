def translate(text: str) -> str:
    """Translates English text into Pig Latin

    :param text: str - text to translate
    :return: str - translated text

    Function that takes in a string to be translated and returns the translated
    text based on set rules.
    """
    VOWELS = "aeiou"

    def translate_word(word: str) -> str:
        """Helper function to implement the translate

        :param word: str - word to translate
        :return: str - translated word
        """
        if word.startswith(("xr", "yt")):
            return word + "ay"
        if word[0] in VOWELS:
            return word + "ay"

        i = 0

        while i < len(word):
            if word[i : i + 2] == "qu":
                i += 2
                continue
            if word[i] in VOWELS or (word[i] == "y" and i != 0):
                break
            i += 1

        return word[i:] + word[:i] + "ay"

    return " ".join(translate_word(word) for word in text.split())
