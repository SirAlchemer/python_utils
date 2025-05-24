
def get_int(prompt: str, valids: tuple[int] = None) -> int:
    while True:
        integer = input(prompt)
        try:
            integer = int(integer)
            if valids == None or integer in valids:
                return integer
            print(f'{integer} is not among the valid integers!: {valids}')
        except ValueError:
            print(f'{integer} is not among the valid integers!: {valids}')

def get_num(prompt: str, valids: tuple[float | int] = None) -> float | int:
    while True:
        integer = input(prompt)
        try:
            integer = eval(integer)
            if valids == None or integer in valids:
                return integer
            print(f'{integer} is not among the valid numbers!: {valids}')
        except ValueError:
            print(f'{integer} is not a valid number!: {valids}')
