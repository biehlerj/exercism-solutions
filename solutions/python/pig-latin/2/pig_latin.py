import re

RE = re.compile("^(x(?!r)|y(?!t)|[^aeiouqxy]*(?:qu?)?)(.+)$")


def translate(text: str) -> str:
    """Translates English text into Pig Latin

    :param text: str - text to translate
    :return: str - translated text

    Function that takes in a string to be translated and returns the translated
    text based on set rules. (Using regex method)
    """

    def translate_word(word: str) -> str:
        """Helper function to implement the translate

        :param word: str - word to translate
        :return: str - translated word
        """
        return RE.sub(lambda w: "{1}{0}ay".format(*w.groups()), word)

    return " ".join(map(translate_word, text.split()))
