import args_parser
import encryptor
import json


def init():
    init_data = bytes(json.dumps({}), encoding='utf8')

    encryptor.encrypt(args_parser.args.mp, init_data)

    print("Password manager initialised")


init()
