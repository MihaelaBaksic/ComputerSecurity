from login.args import args
from getpass import getpass
from login.forcepass_user import update
from db_manip import get_records
from util import verify_hash
from argon2.exceptions import VerifyMismatchError

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
            db_pass_hash = db_record[1]

            # Validating the provided password against the stored hash
            # Raises VerifyMismatchError if verification has failed
            valid = verify_hash(db_pass_hash, password)

            # If validity flag is set to false, perform password reset
            if not db_record[0]:
                update(args.username)

            print("Login successful")
            exit(0)

        except (KeyError, RuntimeError, VerifyMismatchError):
            print("Username or password incorrect")
            attempt_cnt -= 1

        except ValueError as e:
            print(e)
            exit(0)

    if attempt_cnt == 0:
        print("Login failed")
