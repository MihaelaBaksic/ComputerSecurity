from util import *
import db_manip


# Requests user to update the password
def update(username: str):
    data = db_manip.get_records()

    print("Your password has been invalidated by administration, please create a new password for your account: ")
    valid, password = get_password("New password: ")
    if not valid:
        raise ValueError('Password update failed. Password mismatch.')

    if not validate_password(password):
        raise ValueError(
            "User add failed. Password must be at least 8 characters long,\ncontain at least one number and one upper case letter")

        # Hash and store new password
    pass_hash, salt = calculate_hash(password)

    data[username] = (True, salt, pass_hash)
    db_manip.store_records(data)
