
class Dicts:
    char_to_num = {chr(i): i - 96 for i in range(97, 123)}  # Lowercase a-z
    char_to_num.update({chr(i): i - 64 for i in range(65, 91)})  # Uppercase A-Z

    num_to_char = {i: chr(i + 96) for i in range(1, 27)}  # Lowercase a-z
    num_to_char.update({i: chr(i + 64) for i in range(1, 27)})  # Uppercase A-Z
