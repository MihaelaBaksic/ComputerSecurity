from mgmt import db_manip
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
from getpass import getpass


def add(username: str):
    data = db_manip.get_records()

    try:
        data[username]
        print("Username {} already exists. If you wish to update its password use action passwd.".format(username))
    except KeyError:
        password = getpass("Password: ")
        passwordRepeated = getpass("Repeat password: ")

        if password != passwordRepeated:
            print("User add failed. Password mismatch.")
            return

        salt = str(get_random_bytes(16))
        pass_hash = SHA256.new(bytes(password + salt, encoding='utf-8')).hexdigest()

        data[username] = (True, salt, pass_hash)
        db_manip.store_records(data)
        print("Password for username {} successfully added.".format(username))
