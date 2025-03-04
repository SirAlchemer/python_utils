
import json
import pickle
from typing import Any
from . import encryption_utils as enc

def load_from_json(filename: str, dev: bool = False) -> dict:
    """
    Loads data from a JSON file at the specified path.

    Args:
        filename (str): The name of the JSON file to load from.
        path (str): The path to the key in the JSON file to load from. Use dot notation for nested keys (e.g. "player.name").
        dev (bool, optional): Whether to print error messages if the file is not found or the JSON is invalid. Defaults to False.

    Returns:
        Any: The loaded data, or None if the file is not found or the JSON is invalid.
    """
    data = None
    # Try to open the JSON file and load its contents
    try:
        # Try to open the file in read mode
        with open(filename, "r") as file:
            # Load the JSON data from the file
            data = json.load(file)
    except FileNotFoundError:
        # If the file is not found, print an error message if dev is True and return None
        if dev:
            print(f"File '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        # If the JSON is invalid, print an error message if dev is True and return None
        if dev:
            print(f"Error parsing JSON in file '{filename}'.")
        return None

    # Determine the type of the loaded data
    return data


def save_to_json(filename: str, path: str, data) -> None:
    """
    Saves data to a JSON file at the specified path.

    Args:
        filename (str): The name of the JSON file to save to.
        path (str): The path to the key in the JSON file to save to. Use dot notation for nested keys (e.g. "player.name").
        data: The data to save to the JSON file.

    Returns:
        None
    """

    # Try to open the JSON file and load its contents
    try:
        # Try to open the file in read mode
        with open(filename, "r") as file:
            # Load the JSON data from the file
            existing_data = json.load(file)
    except FileNotFoundError:
        # If the file does not exist, create an empty dictionary
        existing_data = {}
    except json.JSONDecodeError:
        # If the file is not valid JSON, create an empty dictionary
        existing_data = {}

    # Split the path into individual keys
    keys = path.split(".")

    # Initialize the current data to the existing data
    current_data = existing_data

    # Iterate through the keys, creating a new dictionary if the key does not exist
    for key in keys[:-1]:
        # Check if the current data is a list
        if isinstance(current_data, list):
            # Try to convert the key to an integer
            try:
                key = int(key)
            except ValueError:
                # If the key is not a valid integer, print an error message and return
                print(f"Invalid path '{path}'")
                return
            # Check if the key is within the bounds of the list
            if key < 0 or key >= len(current_data):
                # If the key is out of bounds, print an error message and return
                print(f"Invalid path '{path}'")
                return
            # If the key is equal to the length of the list, append a new dictionary
            if key == len(current_data):
                current_data.append({})
            # Update the current data to the value at the current key
            current_data = current_data[key]
        # Check if the current data is a dictionary and the key does not exist
        elif isinstance(current_data, dict) and key not in current_data:
            # Create a new dictionary at the current key
            current_data[key] = {}
        # Check if the current data is a dictionary and the key exists
        elif isinstance(current_data, dict) and key in current_data:
            # Update the current data to the value at the current key
            current_data = current_data[key]
        else:
            # If the current data is not a dictionary or list, print an error message and return
            print(f"Invalid path '{path}'")
            return

    # Check if the path has only one key
    if len(keys) == 1:
        # Check if the current data is a list
        if isinstance(current_data, list):
            # Append the data to the list
            current_data.append(data)
        # Check if the current data is a dictionary
        elif isinstance(current_data, dict):
            # Set the value of the key to the data
            current_data[path] = data
        else:
            # If the current data is not a dictionary or list, print an error message and return
            print(f"Invalid path '{path}'")
            return
    else:
        # Check if the current data is a list
        if isinstance(current_data, list):
            # Try to convert the last key to an integer
            try:
                key = int(keys[-1])
            except ValueError:
                # If the key is not a valid integer, print an error message and return
                print(f"Invalid path '{path}'")
                return
            # Check if the key is within the bounds of the list
            if key < 0 or key >= len(current_data):
                # If the key is out of bounds, print an error message and return
                print(f"Invalid path '{path}'")
                return
            # Set the value of the key to the data
            current_data[key] = data
        # Check if the current data is a dictionary
        elif isinstance(current_data, dict):
            # Set the value of the key to the data
            current_data[keys[-1]] = data
        else:
            # If the current data is not a dictionary or list, print an error message and return
            print(f"Invalid path '{path}'")
            return

    # Save the updated data to the JSON file
    with open(filename, "w") as file:
        json.dump(existing_data, file, indent=4)


def delete_json_data(filename):
    with open(filename, "w") as file:
        file.write("")


def load_from_bin(filename: str, dev: bool = False) -> dict:
    data = {}
    try:
        with open(filename, "rb") as file:
            data = file.read()
    except FileNotFoundError:
        if dev == True:
            print(f"File '{filename}' not found.")
        return None
    except Exception as e:
        if dev == True:
            print(f"Error reading file '{filename}': {e}")
        return None

    # Since we're reading binary data, we need to deserialize it into a Python object
    try:
        data = pickle.loads(data)
    except Exception as e:
        if dev == True:
            print(f"Error deserializing data from file '{filename}': {e}")
        return None
    return data


def save_to_bin(filename: str, path: str, data):
    """

    """
    try:
        # trys to open file if no file or data exists it creates a file with an empty dict
        with open(filename, "rb") as file:
            existing_data = pickle.load(file)
    except FileNotFoundError:
        existing_data = {}
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
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

    with open(filename, "wb") as file:
        pickle.dump(existing_data, file)


def encrypted_bin_save(filename, path, data):
    encrypted_data = enc.encrypt(str(data))
    save_to_bin(filename, path, encrypted_data)


def encrypted_bin_load(filename, path) -> Any:
    encrypted_data = load_from_bin(filename, path)
    data = enc.decrypt(encrypted_data)
    return data
