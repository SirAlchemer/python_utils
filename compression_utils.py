import zlib
import base64
import sys
from typing import Any

try:
    import numpy as np
    import cryptography
except ImportError:
    np = None
    cryptography = None


### ----- MISC ----- ###


def __convert_string_value(value: str) -> Any:
    """
    Convert a string value to its appropriate type (int, float, bool, None, or str).
   
    Args:
        value (str): The string value to convert.
       
    Returns:
        Any: The converted value.
    """
    if value.isdigit():
        value = int(value)
    elif value.replace('.', '', 1).isdigit() and value.count('.') == 1:
        value = float(value)
    elif value in ['True', 'true']:
        value = True
    elif value in ['False', 'false']:
        value = False
    elif value in ['None', 'none', 'null']:
        value = None
    else:
        value = value
    return value
   
def get_valid_imports() -> dict[str, bool]:
    """
    Return a dictionary indicating which optional imports are available.
   
    Returns:
        dict[str, bool]: A dictionary with the import names as keys and their availability as values.
    """
    valids = {}
    if np is not None:
        valids['np'] = True
    if cryptography is not None:
        valids['cryptography'] = True
    return valids    
       
### ----- COMPRESSION ----- ###


def __compress_string(string: str) -> str:
    """
    Compress a string using zlib and base64 encoding.
   
    Args:
        string (str): The string to compress.
       
    Returns:
        str: The compressed string in base64 encoding.
    """
    compressed_data = zlib.compress(string.encode())
    compressed_data_b64 = base64.b64encode(compressed_data).decode('utf-8')
    return compressed_data_b64


def __compress_list(list_) -> str:
    """
    Compress a list by converting it to a string and then compressing the string.
   
    Args:
        list_ (list): The list to compress.
       
    Returns:
        str: The compressed string in base64 encoding.
    """
    list_string = ''
    for item in list_:
        list_string += f'{item},'
    list_string = list_string.rstrip(',')
    return __compress_string(list_string)


def __compress_dict(dict_) -> str:
    """
    Compress a dictionary by converting it to a string and then compressing the string.
   
    Args:
        dict_ (dict): The dictionary to compress.
       
    Returns:
        str: The compressed string in base64 encoding.
    """
    dict_string = ''
    for key, value in dict_.items():
        dict_string += f'{key}:{value},'
    dict_string = dict_string.rstrip(',')
    return __compress_string(dict_string)


### ----- DECOMPRESSION ----- ###


def __decompress_string(string: str) -> str:
    """
    Decompress a base64 and zlib compressed string.
   
    Args:
        string (str): The compressed string in base64 encoding.
       
    Returns:
        str: The decompressed string.
    """
    decompressed_data = zlib.decompress(base64.b64decode(string)).decode('utf-8')
    return decompressed_data


def __decompress_dict(dict_string: str) -> dict:
    """
    Decompress a string to a dictionary.
   
    Args:
        dict_string (str): The compressed string in base64 encoding.
       
    Returns:
        dict: The decompressed dictionary.
    """
    dict_string = __decompress_string(dict_string)
    parsed_dict = {}
    for key_value in dict_string.split(','):
        key_value = key_value.split(':')
        parsed_dict[key_value[0]] = __convert_string_value(key_value[1])
    return parsed_dict
   
def __decompress_list(list_string: str) -> list:
    """
    Decompress a string to a list.
   
    Args:
        list_string (str): The compressed string in base64 encoding.
       
    Returns:
        list: The decompressed list.
    """
    list_string = __decompress_string(list_string)
    return [__convert_string_value(val)
            for val in list_string.split(',')]
           
def __decompress_array(array_string: str) -> list:
    """
    Decompress a string to a numpy array.
   
    Args:
        array_string (str): The compressed string in base64 encoding.
       
    Returns:
        list: The decompressed numpy array.
    """
    array_string = __decompress_string(array_string)
    return np.array([__convert_string_value(val)
            for val in array_string.split(',')])
            
            
### ----- CRYPTOGRAPHY ----- ###

from cryptography.fernet import Fernet

# Key generation (run once and store the key securely)
def generate_key() -> bytes:
    """
    Generate a new Fernet key. This should only be done once and securely stored.
    """
    return Fernet.generate_key()

# Encrypt function
def encrypt(data: str, key: bytes) -> str:
    """
    Encrypt a string using Fernet symmetric encryption.

    Args:
        data (str): The string to encrypt.
        key (bytes): The Fernet key for encryption.

    Returns:
        str: The encrypted string.
    """
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data.decode()

# Decrypt function
def decrypt(encrypted_data: str, key: bytes) -> str:
    """
    Decrypt a string using Fernet symmetric encryption.

    Args:
        encrypted_data (str): The encrypted string to decrypt.
        key (bytes): The Fernet key for decryption.

    Returns:
        str: The decrypted string.
    """
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data.encode())
    return decrypted_data.decode()


### ----- MAIN FUNCTIONS ----- ###

def compress(data: Any, key: bytes = None, **kwargs) -> str:
    """
    Compress data (string, list, dict, or numpy array) and return the compressed string.
   
    Args:
        data (Any): The data to compress (str, list, dict, or numpy array).
        key (bytes): Optional encryption key for encrypting the compressed data.
       
    Returns:
        str: The compressed (and optionally encrypted) string in base64 encoding.
       
    Raises:
        TypeError: If the data type is unsupported.
    """
    valid_imports = get_valid_imports()
    if type(data) == str:
        data = __compress_string(data)
    elif type(data) == dict:
        data = __compress_dict(data)
    elif type(data) == list:
        data = __compress_list(data)
    if valid_imports.get('np', False):
        if type(data) == np.ndarray:
            data = __compress_list(data)
   
    while True:
        if sys.getsizeof(__compress_string(data)) < sys.getsizeof(data):
            data = __compress_string(data)
            print('extra compression!')
        else:
            if key:
                data = encrypt(data, key)
            return data
   
def decompress(string: str, key: bytes = None, type_=str, **kwargs) -> Any:
    """
    Decompress a string to its original data type (string, list, dict, or numpy array).
   
    Args:
        string (str): The compressed (and optionally encrypted) string.
        key (bytes): Optional decryption key to decrypt the string before decompression.
        type_ (type or str): The type to which the string should be decompressed (str, list, dict, or numpy array).
       
    Returns:
        Any: The decompressed data.
       
    Raises:
        TypeError: If the data type is unsupported.
    """
    if key:
        string = decrypt(string, key)
    string = __decompress_string(string)
    while True:
        try:
            string = __decompress_string(string)
            print('extra decompression!')
        except Exception:
            string = __compress_string(string)
            break
        
    valid_imports = get_valid_imports()
    if type_ == str:
        data = __decompress_string(string)
    elif type_ == dict:
        data = __decompress_dict(string)
    elif type_ == list:
        data = __decompress_list(string)
    if valid_imports.get('np', False):
        if type_ == np.ndarray or type_ == np.array:
            data = __decompress_array(string)
    return data
