import string

CIPHER = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1])


def encode(plain_text: str):
    """Encodes text using Atbash cipher

    :param plain_text: str - text to encode
    :return: str - Atbash encoded text

    v2 updates to use one cipher constant
    """

    translated = "".join(
        char for char in plain_text.lower() if char.isalnum()
    ).translate(CIPHER)

    return " ".join(
        translated[index : index + 5] for index in range(0, len(translated), 5)
    )


def decode(ciphered_text: str):
    """Decodes text using the Atbash cipher

    :param ciphered_text: str - Atbash encoded string
    :return: str - decoded string

    v2 updates to use one cipher constant
    """

    return "".join(char.lower() for char in ciphered_text if char.isalnum()).translate(
        CIPHER
    )
