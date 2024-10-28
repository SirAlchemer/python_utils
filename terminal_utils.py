import os
import platform
import subprocess
import sys


# ______clear_terminal_______#
def clear_terminal():
    """
    Clears the terminal screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


# ______get_terminal_size_______#
def get_terminal_size():
    """
    Returns the size of the terminal in characters.
    """
    try:
        return subprocess.check_output(["stty", "size"]).decode().split()
    except:
        return [25, 80]  # default size


# ______get_terminal_width_______#
def get_terminal_width():
    """
    Returns the width of the terminal in characters.
    """
    return int(get_terminal_size()[1])


# ______get_terminal_height_______#
def get_terminal_height():
    """
    Returns the height of the terminal in characters.
    """
    return int(get_terminal_size()[0])


# ______get_operating_system_______#
def get_operating_system():
    """
    Returns the name of the operating system.
    """
    return platform.system()


# ______get_terminal_type_______#
def get_terminal_type():
    """
    Returns the type of terminal.
    """
    return os.environ.get("TERM")


# ______get_python_version_______#
def get_python_version():
    """
    Returns the version of Python.
    """
    return sys.version


# ______print_centered_text_______#
def print_centered_text(text):
    """
    Prints the given text centered in the terminal.
    """
    width = get_terminal_width()
    padding = " " * ((width - len(text)) // 2)
    print(padding + text)


# ______print_horizontal_line_______#
def print_horizontal_line(char="-", width=None):
    """
    Prints a horizontal line of the given character.
    """
    if width is None:
        width = get_terminal_width()
    print(char * width)


# ______print_vertical_line_______#
def print_vertical_line(char="|", height=None):
    """
    Prints a vertical line of the given character.
    """
    if height is None:
        height = get_terminal_height()
    for _ in range(height):
        print(char)


# ______print_box_______#
def print_box(text, char="-", width=None, height=None):
    """
    Prints a box with the given text.
    """
    if width is None:
        width = get_terminal_width()
    if height is None:
        height = get_terminal_height()
    print_horizontal_line(char, width)
    for _ in range(height - 2):
        print(char + " " * (width - 2) + char)
    print(char + text + char)
    for _ in range(height - 3):
        print(char + " " * (width - 2) + char)
    print_horizontal_line(char, width)
