def get_attr(
    prompt, data_type=str, min_int: int | None = None, max_int: int | None = None,
    custom_error: str | None = None):
    validation_functions = {
        int: lambda x: (min_int is None or x >= min_int) and (max_int is None or x <= max_int),
        float: lambda x: True,
        bool: lambda x: x in [True, False],
        str: lambda x: True
    }

    error_messages = {
        int: lambda x: f"{x} is not a valid integer",
        float: lambda x: f"{x} is not a valid number",
        bool: lambda x: f"{x} is not 'Y' or 'N'",
        str: lambda x: ""
    }

    while True:
        response = input(prompt)
        try:
            response = data_type(response)
            if not validation_functions[data_type](response):
                if custom_error:
                    print(custom_error)
                elif min_int is not None and response < min_int:
                    print(f"{response} is less than {min_int}!")
                elif max_int is not None and response > max_int:
                    print(f"{response} is greater than {max_int}!")
                else:
                    print(error_messages[data_type](response))
            else:
                return response
        except ValueError:
            if custom_error:
                print(custom_error)
            else:
                print(error_messages[data_type](response))
