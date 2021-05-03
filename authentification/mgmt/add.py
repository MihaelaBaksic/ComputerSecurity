import db_manip
from util import *


# Adding new username and password to database
def add(username: str):
    data = db_manip.get_records()

    try:
        data[username]
        print("Username {} already exists. If you wish to update its password use action passwd.".format(username))
    except KeyError:

        valid, password = get_password("Password: ")
        if not valid:
            print("User add failed. Password mismatch.")
            return

        if not validate_password(password):
            print("User add failed. Password must be at least 8 characters long,\ncontain at least one number and one upper case letter")
            return

        # Hashing and storing password into database
        pass_hash, salt = calculate_hash(password)

        data[username] = (True, salt, pass_hash)
        db_manip.store_records(data)
        print("Password for username {} successfully added.".format(username))
