try:
    from cryptography.fernet import Fernet
except ImportError:
    print("CRITICAL IMPORT ERROR: 'cryptography.fernet' NOT FOUND!!!")


def encrypt(data):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    data = cipher.encrypt(str(data).encode('utf-8'))  # Convert data to bytes
    fernet_data = [key, data]
    return fernet_data

def decrypt(encrypted_data):
    key, data = encrypted_data
    cipher = Fernet(key)
    data = cipher.decrypt(data).decode('utf-8')  # Decode data back to string
    return data
    
