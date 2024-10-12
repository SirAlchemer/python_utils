import math


# ______is_even_number_______#
def is_even_number(number: int):
    if number % 2 == 0:
        return True
    else:
        return False


# ______find_gcf_______#
def find_gcf(*args):
    def _find_gcf(a, b):
        return b and _find_gcf(b, a%b) or a

    result = args[0]
    for num in args[1:]:
        result = _find_gcf(result, num)

    return result if result != 1 else None


# ______collatz_sequence_______#
def collatz_sequence(x: int, time: int):
    while True:
        time.sleep(time)
        # number is even so we divide it by 2
        if is_even_number(x) == True:
            x = x // 2
            print("diveded by 2:", x)
        # breaks loop if the sequence is completed
        elif x == 1:
            print(x)
            break
        # number is odd
        else:
            x = (x * 3) + 1
            print(x)
