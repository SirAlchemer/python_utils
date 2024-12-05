

def add_prefix(text, *args):
    """
    Add ANSI escape sequence prefixes to the given text.

    Args:
        text (str): The text to which the prefixes will be added.
        *args (str): Variable number of prefix arguments.

    Returns:
        str: The text with the added prefixes.

    Prefixes:
        black, red, green, yellow, blue, magenta, cyan, white
        bg_black, bg_red, bg_green, bg_yellow, bg_blue, bg_magenta, bg_cyan, bg_white
        bold, underline, inverse

    Example:
        print(add_prefix("Hello, world!", "red", "bg_black", "bold"))
    """

    prefixes = "\033["
    valid_prefixes = {
        "black": "30",
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
        "magenta": "35",
        "cyan": "36",
        "white": "37",
        "bold": "1",
        "underline": "4",
        "inverse": "7",
    }
    valid_bg_prefixes = {
        "bg_black": "40",
        "bg_red": "41",
        "bg_green": "42",
        "bg_yellow": "43",
        "bg_blue": "44",
        "bg_magenta": "45",
        "bg_cyan": "46",
        "bg_white": "47",
    }

    for prefix in args:
        if prefix in valid_prefixes:
            prefixes += f"{valid_prefixes[prefix]};"
        elif prefix in valid_bg_prefixes:
            prefixes += f"{valid_bg_prefixes[prefix]};"
        else:
            raise ValueError(f"Invalid prefix: {prefix}")

    # Remove the trailing semicolon
    prefixes = prefixes.rstrip(";")

    return f"{prefixes}m{text}\033[0m"

