

# ______convert_string_to_list_______#
def convert_string_to_list(string):
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