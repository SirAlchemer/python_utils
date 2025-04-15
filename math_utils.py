
def next_lexicographical_permutation_num(n: int) -> int:
    s = list(str(n))
    for i in range(len(s) - 2, -1, -1):
        if s[i] < s[i + 1]:
            t = s[i:]
            m = min(filter(lambda x: x > t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1

def sqrt(value: float | int, pow=2) -> float | int:
    if pow == 2:
        # If the default is square root
        return value ** 0.5
    else:
        # Return the value raised to the specified power
        return value ** (1 / pow)

def distance_formula(q1: tuple[float | int], q2: tuple[float | int]) -> float | int:
    return abs(sqrt(((q2[0] - q1[0]) ** 2) + (q2[1] - q1[1]) ** 2))

# Lowest common multiplier
def lcm(a, b):
    return abs(a * b) // Fraction.gcd(a, b)
    
# Greatest common denominator
def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

