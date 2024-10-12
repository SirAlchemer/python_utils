from typing import Optional


# ______get_int_______#
def get_int(prompt: Optional[str]) -> int:
    """
    Takes in prompt as an argument and then gains user input
    validating that it is a integer and then returns it
    """
    while True:
        x = input(prompt)  # Input an intiger Ex: 1, 5, 16
        try:
            x = int(x)
            return x
        except ValueError:
            print(f"{x} is not an intiger")


# ______get_float_______#
def get_float(prompt: Optional[str]) -> float:
    """
    Takes in prompt as an argument and then gains user input
    validating that it is a float and then returns it
    """
    while True:
        x = input(prompt)
        try:  # Input a number with a decimal Ex: 3.8, 2.1, 1.0
            x = float(x)
            return x
        except ValueError:
            print(f"{x} is not a float")


# ______get_bool_______#
def get_bool(prompt: Optional[str]) -> bool:
    """
    Takes in prompt as an argument and then gains user input
    validating that it is a boolean and then returns it
    """
    while True:
        x = input(prompt)  # Input True or False
        if x.lower() == "true":
            return True
        elif x.lower() == "false":
            return False
        else:
            print(f"{x} is not a boolean")


# ______get_string_______#
def get_string(prompt: Optional[str]) -> str:
    """
    Takes in prompt as an argument and then gains user input
    validating that it is a non empty string and then returns it
    """
    while True:
        x = input(prompt)  # Input a string
        if x.strip() != "":
            return x
        else:
            print("Please enter a non-empty string")
