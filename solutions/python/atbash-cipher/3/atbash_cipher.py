import string

CIPHER = {
    char: string.ascii_lowercase[id]
    for id, char in enumerate(string.ascii_lowercase[::-1])
}


def encode(text: str, decode: bool = False) -> str:
    """Encodes or decodes text using Atbash cipher

    :param text: str - text to encode
    :param decode: bool - flag for whether to encode or decode the text.
    Default = False
    :return: str - Atbash encoded or decoded text

    v3 uses one function to encode and decode
    """

    translated = "".join(
        CIPHER.get(char, char) for char in text.lower() if char.isalnum()
    )

    return (
        translated
        if decode
        else " ".join(
            translated[index : index + 5] for index in range(0, len(translated), 5)
        )
    )


def decode(ciphered_text: str) -> str:
    """Decodes text using the Atbash cipher

    :param ciphered_text: str - Atbash encoded string
    :return: str - decoded string

    v2 updates to use one cipher constant
    """

    return encode(ciphered_text, True)
