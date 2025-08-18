def encode(numbers: list[int]) -> list[int]:
    """Encodes a list of integers following VLQ encoding

    :param numbers: list[int] - integers to encode
    :return: list[int] - list of encoded integers
    """
    if not numbers:
        return []

    encoded: list[int] = []

    for number in numbers:
        if number < 0 or number > 0xFFFFFFFF:
            raise ValueError("number out of range")

        bytes_ = []

        while True:
            bytes_.insert(0, number & 0x7F)
            number >>= 7

            if number == 0:
                break

        for i in range(len(bytes_) - 1):
            bytes_[i] |= 0x80

        encoded.extend(bytes_)

    return encoded


def decode(bytes_: list[int]) -> list[int]:
    """Decodes a list of integers following VLQ decoding

    :param bytes_: list[int] - integers to decode
    :return: list[int] - decoded integers
    """
    if not bytes_:
        return []

    decoded: list[int] = []
    number = 0

    for _, byte in enumerate(bytes_):
        number = (number << 7) | (byte & 0x7F)

        if not (byte & 0x80):
            decoded.append(number)
            number = 0

    if bytes_ and bytes_[-1] & 0x80:
        raise ValueError("incomplete sequence")

    return decoded
