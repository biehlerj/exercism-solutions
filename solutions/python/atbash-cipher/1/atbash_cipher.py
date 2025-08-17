import string

CIPHER_ENCODE = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1])
CIPHER_DECODE = str.maketrans(string.ascii_lowercase[::-1], string.ascii_lowercase)


def encode(plain_text: str):
    """Encodes text using Atbash cipher

    :param plain_text: str - text to encode
    :return: str - Atbash encoded text
    """

    filtered = [char.lower() for char in plain_text if char.isalnum()]
    translated = "".join(
        [char.translate(CIPHER_ENCODE) if char.isalpha() else char for char in filtered]
    )
    grouped = " ".join(translated[i : i + 5] for i in range(0, len(translated), 5))

    return grouped


def decode(ciphered_text: str):
    """Decodes text using the Atbash cipher

    :param ciphered_text: str - Atbash encoded string
    :return: str - decoded string
    """

    filtered = [char.lower() for char in ciphered_text if char.isalnum()]
    translated = "".join(
        [char.translate(CIPHER_ENCODE) if char.isalpha() else char for char in filtered]
    )

    return translated
