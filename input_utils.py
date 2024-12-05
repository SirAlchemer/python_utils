

def get_attr(prompt, data_type = str):
    while True:
        response = input(prompt)
        if data_type is int:
            try:
                response = int(response)
                return response
            except ValueError:
                print(f"{response} is not a valid intiger")
        elif data_type is float:
            try:
                response = float(response)
                return response
            except ValueError:
                print(f"{response} is not a valid number")
        elif data_type is bool:
            try:
                if response.lower() == "y" or response.lower() == "[y]":
                    return True
                elif response.lower() == "n" or response.lower() == "[n]":
                    return False
                else:
                    raise ValueError()
            except ValueError:
                print(f"{response} is not 'Y' or 'N'")
        else:
            return response
