import args_parser
import encryptor
import json


# Performs database and master password initialization
def init():
    init_data = bytes(json.dumps({}), encoding='utf8')

    # Encrypt initial data and store to database
    encryptor.encrypt(args_parser.args.mp, init_data)

    print("Password manager initialised")


init()
