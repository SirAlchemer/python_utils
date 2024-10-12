from cryptography.fernet import Fernet
import json

def encrypt_data(key, data):
    encrypter = Fernet(key)
    encrypted_data = encrypter.encrypt(data.encode())
    return encrypted_data

def decrypt_data(key, encrypted_data):
    decrypter = Fernet(key)
    decrypted_data = decrypter.decrypt(encrypted_data)
    return decrypted_data.decode()

def encrypted_save(filename, path, data_to_encrypt):
    # Convert the list to a string
    data_to_encrypt = json.dumps(data_to_encrypt)

    # Generate a new key
    key = Fernet.generate_key()
    encrypter = Fernet(key)
    encrypted_data = encrypter.encrypt(data_to_encrypt.encode())

    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    if isinstance(data, dict):
        if path in data:
            data[path].append([key.decode(), encrypted_data.decode()])
        else:
            data[path] = [[key.decode(), encrypted_data.decode()]]

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    else:
        print("Error: Data is not a dictionary.")
        return None

def encrypted_load(filename, path):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON in file '{filename}': {e}")
        return None

    if isinstance(data, dict):
        if path in data:
            decrypted_data = []
            for key, encrypted_data in data[path]:
                key = bytes(key, 'utf-8')
                encrypted_data = bytes(encrypted_data, 'utf-8')

                # Decrypt the data
                decrypter = Fernet(key)
                decrypted_data.append(decrypter.decrypt(encrypted_data).decode())
            return decrypted_data
        else:
            return None
    else:
        return None
