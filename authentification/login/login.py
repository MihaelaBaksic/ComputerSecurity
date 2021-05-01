from login_args import args
from Crypto.Hash import SHA256
from getpass import getpass
from db_manip import get_records
from forcepass_user import update

if __name__ == '__main__':
    try_cnt = 3

    while try_cnt:
        try:
            password = getpass("Password: ")
            data = get_records()

            db_record = data[args.username]

            salt = db_record[1]
            db_pass_hash = db_record[2]
            provided_pass_hash = SHA256.new(bytes(password + salt, encoding='utf-8')).hexdigest()

            if db_pass_hash != provided_pass_hash:
                raise KeyError

            if not db_record[0]:
                update(args.username)

            print("Login successful")
            exit(0)

        except KeyError:
            print("Username or password incorrect")
            try_cnt -= 1
        except ValueError:
            print("Password update failed. Password mismatch.")
            exit(0)
