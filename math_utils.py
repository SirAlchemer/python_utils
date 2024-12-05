import random


def random_float(range1: float | int, range2: float | int, decimals: int = 2) -> float | int:
    flt = f"{random.randint(round(range1), round(range2))}"
    flt += "."
    for i in range(decimals):
        flt += f"{random.randint(1,9)}"
    if float(flt) < range1:
        return range1
    elif float(flt) > range2:
        return range2
    return float(flt)
