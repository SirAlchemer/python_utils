import os


# ______clear_terminal_______#
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")