from getpass import getpass
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
import db_manip


# Requests user to update its password
def update(username: str):
    data = db_manip.get_records()

    print("Your password has been invalidated by administration, please create a new password for your account: ")
    password = getpass("New password: ")
    passwordRepeated = getpass("Repeat new password: ")

    if password != passwordRepeated:
        raise ValueError('Password update failed. Password mismatch.')

    # Hash and store new password
    salt = str(get_random_bytes(16))
    pass_hash = SHA256.new(bytes(password + salt, encoding='utf-8')).hexdigest()

    data[username] = (True, salt, pass_hash)
    db_manip.store_records(data)
