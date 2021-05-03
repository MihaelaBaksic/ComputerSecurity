from login.args import args
from Crypto.Hash import SHA256
from getpass import getpass
from login.forcepass_user import update
from db_manip import get_records
from util import calculate_hash

# Performing user login
# User has 3 attempts to enter a correct password
if __name__ == '__main__':
    attempt_cnt = 3

    while attempt_cnt:
        try:
            password = getpass("Password: ")
            data = get_records()

            db_record = data[args.username]

            # Fetching stored salt and password hash from database
            salt = db_record[1]
            db_pass_hash = db_record[2]

            # Calculating password hash from provided password and stored hash
            provided_pass_hash, _ = calculate_hash(password, salt)

            # Comparing provided and stored password hash
            if db_pass_hash != provided_pass_hash:
                raise RuntimeError

            # If validity flag is set to false, perform password reset
            if not db_record[0]:
                update(args.username)

            print("Login successful")
            exit(0)

        except (KeyError, RuntimeError):
            print("Username or password incorrect")
            attempt_cnt -= 1

        except ValueError:
            print("Password update failed. Password mismatch.")
            exit(0)

    if attempt_cnt == 0:
        print("Login failed")
