from getpass import getpass
from util import calculate_hash
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
    pass_hash, salt = calculate_hash(password)

    data[username] = (True, salt, pass_hash)
    db_manip.store_records(data)
