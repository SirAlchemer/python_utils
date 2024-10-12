

def create_dict(keys, datas, is_global=False):
    data_library = {}

    for key_data in zip(keys, datas):
        add_to_dict = list(key_data)
        data_library[add_to_dict[0]] = add_to_dict[1]

    if is_global:
        globals(data_library)
    else:
        return data_library

    []
