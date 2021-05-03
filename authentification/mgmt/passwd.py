from getpass import getpass
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
import db_manip
from util import calculate_hash


# Updating password of an existing user
def passwd(username: str):
    data = db_manip.get_records()

    try:
        password = getpass("Password: ")
        passwordRepeated = getpass("Repeat password: ")

        if password != passwordRepeated:
            print("Password update failed. Password mismatch.")
            return

        # Hashing and storing new password to the database
        pass_hash, salt = calculate_hash(password)

        data[username][1:] = (salt, pass_hash)
        db_manip.store_records(data)

        print("Password for username {} successfully updated.".format(username))

    except KeyError:
        print("Username {} doesn't exists in the database. If you wish to add it use action add.".format(username))
