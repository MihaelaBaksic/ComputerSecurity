import db_manip
from util import *


# Updating password of an existing user
def passwd(username: str):
    data = db_manip.get_records()

    try:
        valid, password = get_password("Password: ")
        if not valid:
            print("Password update failed. Password mismatch.")
            return

        if not validate_password_format(password):
            print("Password update failed. Password must be at least 8 characters long,\ncontain at least one number and one upper case letter")
            return

        # Hashing and storing new password to the database
        pass_hash = calculate_hash(password)

        data[username][1] = pass_hash
        db_manip.store_records(data)

        print("Password for username {} successfully updated.".format(username))

    except KeyError:
        print("Username {} doesn't exists in the database. If you wish to add it use action add.".format(username))
