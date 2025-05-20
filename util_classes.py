
class Dicts:
    # Create mappings for lowercase a-z
    char_to_num = {chr(i): i - 96 for i in range(97, 123)}
    # Add mappings for uppercase A-Z
    char_to_num.update({chr(i): i - 64 for i in range(65, 91)})
    # Add mappings for special characters
    special_chars = "!@#$%^&*()-_=+[]{}|;:',.<>?/~`"
    char_to_num.update({char: idx + 53 for idx, char in enumerate(special_chars)})  # Start numbering after 52

    # Create mappings for numbers 1-26 to lowercase a-z
    num_to_char = {i: chr(i + 96) for i in range(1, 27)}
    # Add mappings for numbers 1-26 to uppercase A-Z
    num_to_char.update({i + 26: chr(i + 64) for i in range(1, 27)})
    # Add mappings for special characters
    num_to_char.update({idx + 53: char for idx, char in enumerate(special_chars)})

class ANSI_Codes:
    END_ANSI = "\033[0m"
    BOLD = '\033[1m'
    DARK_GRAY = '\033[2m'
    ITALICS = '\033[3m'
    UNDERLINE = '\033[4m'
    WHITE_BACKGROUND = '\033[7m'
    BLACK = '\033[8m'
    STRIKE_THROUGH = '\033[9m'
    DOUBLE_UNDERLINE = '\033[21m'
    RED = '\033[31m'
    GRAY = '\033[30m'
    MINT = '\033[32m'
    YELLOW = '\033[33m'
    CYAN = '\033[34m'
    MAGENTA = '\033[35m'
    WHITE = '\033[37m'
    RED_BACKGROUND = '\033[41m'
    MINT_BACKGROUND = '\033[42m'
    YELLOW_BACKGROUND = '\033[43m'
    BlUE_BACKGROUND = '\033[44m'
    MAGENTA_BACKGROUND = '\033[45m'
    CYAN_BACKGROUND = '\033[46m'
    WHITE_BACKGROUND = '\033[47m'
    OVER_LINE = '\033[53m'
    LIGHT_RED = "\033[91m"
    GRAY_BACKGROUND = "\033[100m"
    LIGHT_RED_BACKGROUND = "\033[101m"

class Chars:
    LOWER_ALPHA = 'abcdefghijklmnopqrstuvwxyz'
    UPPER_ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    MIXED_ALPHA = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LOWER_ALPHA_NUMERIC = 'abcdefghijklmnopqrstuvwxyz0123456789'
    UPPER_ALPHA_NUMERIC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    MIXED_ALPHA_NUMERIC = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    NUMERIC = '0123456789'
    MISC = r'`~@#$%^&*()_-+={[}]|\;:"<,>.?/' + "'"
    ALL = r'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~@#$%^&*()_-+={[}]|\;:"<,>.?/' + "'"

