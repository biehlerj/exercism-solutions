COMMANDS = ["wink", "double blink", "close your eyes", "jump"]


def commands(binary_str: str):
    """Executes a series of commands based on a provided binary

    :param binary_str: str - binary code to interpret
    :return: list[str] - the commands to be executed
    """

    bits = binary_str.zfill(5)[-5:]
    actions = []

    for i in range(4):
        if bits[4 - i] == "1":
            actions.append(COMMANDS[i])

    if bits[0] == "1":
        actions.reverse()

    return actions
