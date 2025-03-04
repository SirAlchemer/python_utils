def get_int(prompt: str, valids: list[int] = None):
    while True:
        try:
            integer = int(input(prompt))
            if not valids or integer in valids:
                return integer
            else:
                print(f'{integer} is not in the valid integers. ({", ".join(valids)})')
        except (ValueError, TypeError):
            print(f'{integer} is not a valid integer. Please enter a vaild integer.')
