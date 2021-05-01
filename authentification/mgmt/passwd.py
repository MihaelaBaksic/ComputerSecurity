from mgmt import db_manip
from getpass import getpass
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256


def passwd(username: str):
    data = db_manip.get_records()

    try:
        password = getpass("Password: ")
        passwordRepeated = getpass("Repeat password: ")

        if password != passwordRepeated:
            print("Password update failed. Password mismatch.")
            return

        salt = str(get_random_bytes(16))
        pass_hash = SHA256.new(bytes(password + salt, encoding='utf-8')).hexdigest()
        print(pass_hash)

        data[username][1:] = (salt, pass_hash)
        db_manip.store_records(data)

        print("Password for username {} successfully updated.".format(username))
    except KeyError:
        print("Username {} doesn't exists in the database. If you wish to add it use action add.".format(username))
