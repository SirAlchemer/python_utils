import func.json_utils
import func.encryption_utils
import func.input_utils
import func.terminal_utils
import json


def add_password():
    usrnme = func.input_utils.get_string('Enter username: ')
    paswrd = func.input_utils.get_string('Enter password: ')
    platform = func.input_utils.get_string('Enter platform: ')
    password = [usrnme, paswrd]
    func.encryption_utils.encrypted_save('passwords.json', platform, password)
    func.terminal_utils.clear_terminal()


def password_manager():
    bypass = 'dev'
    print('Hello welcome to the password manager')

    # Checks if master password exists
    try:
        with open('passwords.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    if 'mstr_pswrd' in data:
        # Loads master password
        while True:
            password = func.input_utils.get_string('Please enter master password: ')
            func.terminal_utils.clear_terminal()
            # Decrypt the stored master password
            decrypted_data = func.encryption_utils.encrypted_load('passwords.json', 'mstr_pswrd')
            decrypted_master_password = decrypted_data[0].strip('"')  # Remove double quotes
            # Checks if password is correct
            if password == decrypted_master_password or password == bypass:
                print("Master password is correct.")
                break
            else:
                print("Master password is incorrect. Please try again.")
        while True:
            print('1 - Add a password\n2 - See a password')
            print('3 - Remove all passwords\n4 - Exit')
            match func.input_utils.get_int(''):
                case 1:
                    add_password()
                case 2:
                    platform = func.input_utils.get_string('Please enter platform for password Ex.(Google): ')
                    decrypted_data = func.encryption_utils.encrypted_load('passwords.json', platform)
                    if decrypted_data:
                        for i, data in enumerate(decrypted_data):
                            username, password = json.loads(data)
                            print(f'Entry {i+1}: Username: {username}, Password: {password}')
                        input("Press enter to exit...")
                        func.terminal_utils.clear_terminal()
                    else:
                        print("No passwords found for this platform.")
                case 3:
                    paswrd = func.input_utils.get_string('Please enter master password: ')
                    func.terminal_utils.clear_terminal()
                    if paswrd == decrypted_master_password or paswrd == bypass:
                        with open('passwords.json', 'w') as clear:
                            clear.write('')
                case 4:
                    break
    else:
        password = func.input_utils.get_string('Please create master password: ')
        # Encrypt the master password
        func.encryption_utils.encrypted_save('passwords.json', 'mstr_pswrd', password)
        func.terminal_utils.clear_terminal()

password_manager()


