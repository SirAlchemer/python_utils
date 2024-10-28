import re


# ______convert_string_to_list_______#
def convert_string_to_list(string):
    """
    Converts a string into a list of words and numbers.
    """
    # Split the input string into words
    words = string.split()
    # Initialize an empty list to store the result
    result = []
    # Iterate over each word in the list of words
    for word in words:
        # Check if the word is a number
        if word.replace(".", "", 1).replace("-", "", 1).isdigit():
            # If the word is a number, convert it to a float and add it to the result list
            result.append(float(word))
        else:
            # If the word is not a number, add it to the result list as is
            result.append(word)

    return result


# ______convert_string_to_int_list_______#
def convert_string_to_int_list(string):
    """
    Converts a string into a list of integers.
    """
    # Split the input string into words
    words = string.split()
    # Initialize an empty list to store the result
    result = []
    # Iterate over each word in the list of words
    for word in words:
        # Check if the word is a number
        if word.replace("-", "", 1).isdigit():
            # If the word is a number, convert it to an integer and add it to the result list
            result.append(int(word))

    return result


# ______convert_string_to_float_list_______#
def convert_string_to_float_list(string):
    """
    Converts a string into a list of floats.
    """
    # Split the input string into words
    words = string.split()
    # Initialize an empty list to store the result
    result = []
    # Iterate over each word in the list of words
    for word in words:
        # Check if the word is a number
        if word.replace(".", "", 1).replace("-", "", 1).isdigit():
            # If the word is a number, convert it to a float and add it to the result list
            result.append(float(word))

    return result


# ______convert_string_to_bool_list_______#
def convert_string_to_bool_list(string):
    """
    Converts a string into a list of boolean values.
    """
    # Split the input string into words
    words = string.split()
    # Initialize an empty list to store the result
    result = []
    # Iterate over each word in the list of words
    for word in words:
        # Check if the word is a boolean value
        if word.lower() == "true":
            # If the word is "true", add True to the result list
            result.append(True)
        elif word.lower() == "false":
            # If the word is "false", add False to the result list
            result.append(False)

    return result


# ______convert_string_to_list_with_regex_______#
def convert_string_to_list_with_regex(string, pattern):
    """
    Converts a string into a list of matches using a regular expression pattern.
    """
    # Compile the regular expression pattern
    regex = re.compile(pattern)
    # Find all matches in the input string
    matches = regex.findall(string)
    # Return the list of matches
    return matches


# ______strip_string_______#
def strip_string(string):
    """
    Removes leading and trailing whitespace from a string.
    """
    return string.strip()


# ______trim_string_______#
def trim_string(string):
    """
    Removes leading and trailing whitespace from a string.
    """
    return string.strip()


# ______remove_whitespace_______#
def remove_whitespace(string):
    """
    Removes all whitespace from a string.
    """
    return string.replace(" ", "")


# ______remove_newlines_______#
def remove_newlines(string):
    """
    Removes all newline characters from a string.
    """
    return string.replace("\n", "")


# ______remove_tabs_______#
def remove_tabs(string):
    """
    Removes all tab characters from a string.
    """
    return string.replace("\t", "")


# ______split_string_______#
def split_string(string, separator):
    """
    Splits a string into a list of substrings using a separator.
    """
    return string.split(separator)


# ______join_strings_______#
def join_strings(strings, separator):
    """
    Joins a list of strings into a single string using a separator.
    """
    return separator.join(strings)


# ______replace_string_______#
def replace_string(string, old, new):
    """
    Replaces all occurrences of a substring in a string with a new substring.
    """
    return string.replace(old, new)


# ______count_substring_______#
def count_substring(string, substring):
    """
    Counts the number of occurrences of a substring in a string.
    """
    return string.count(substring)


# ______find_substring_______#
def find_substring(string, substring):
    """
    Finds the index of the first occurrence of a substring in a string.
    """
    return string.find(substring)


# ______index_substring_______#
def index_substring(string, substring):
    """
    Finds the index of the first occurrence of a substring in a string.
    """
    return string.index(substring)
