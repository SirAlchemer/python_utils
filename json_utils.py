import json

def load_from_json(filename: str, path: str, dev: bool = False):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        if dev == True:
            print(f"File '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        if dev == True:
            print(f"Error parsing JSON in file '{filename}'.")
        return None

    if isinstance(data, dict):
        data_type = 'dict'
    elif isinstance(data, list):
        data_type = 'list'
    else:
        data_type = 'single'

    if data_type == 'dict':
        return data.get(path)
    elif data_type == 'list':
        if path.isdigit() and 0 <= int(path) < len(data):
            return data[int(path)]
        else:
            raise ValueError("Invalid key for list")
    elif data_type == 'single':
        if path == 'value':
            return data
        else:
            raise ValueError("Invalid key for single value")
    else:
        raise ValueError("Invalid data type")


def save_to_json(filename: str, path: str, data):
    """

    """
    try:
        # trys to open file if no file or data exists it creates a file with an empty dict
        with open(filename, "r") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}
    except json.JSONDecodeError:
        existing_data = {}


    keys = path.split(".")
    current_data = existing_data
    for key in keys[:-1]:
        if isinstance(current_data, list):
            try:
                key = int(key)
            except ValueError:
                print(f"Invalid path '{path}'")
                return
            if key < 0 or key >= len(current_data):
                print(f"Invalid path '{path}'")
                return
            if key == len(current_data):
                current_data.append({})
            current_data = current_data[key]
        elif isinstance(current_data, dict) and key not in current_data:
            current_data[key] = {}
        elif isinstance(current_data, dict) and key in current_data:
            current_data = current_data[key]
        else:
            print(f"Invalid path '{path}'")
            return

    if len(keys) == 1:
        if isinstance(current_data, list):
            current_data.append(data)
        elif isinstance(current_data, dict):
            current_data[path] = data
        else:
            print(f"Invalid path '{path}'")
            return
    else:
        if isinstance(current_data, list):
            try:
                key = int(keys[-1])
            except ValueError:
                print(f"Invalid path '{path}'")
                return
            if key < 0 or key >= len(current_data):
                print(f"Invalid path '{path}'")
                return
            current_data[key] = data
        elif isinstance(current_data, dict):
            current_data[keys[-1]] = data
        else:
            print(f"Invalid path '{path}'")
            return

    with open(filename, "w") as file:
        json.dump(existing_data, file, indent=4)
