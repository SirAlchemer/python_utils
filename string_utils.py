
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

def next_lexicographical_permutation(s: str) -> str:
    s = list(s)
    for i in range(len(s) - 2, -1, -1):
        if ord(s[i]) < ord(s[i + 1]):
            t = s[i:]
            m = min(filter(lambda x:  ord(x) >  ord(t[0]), t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return "".join(s)
    return ""
