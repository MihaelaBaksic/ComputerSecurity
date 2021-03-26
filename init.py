import args_parser
import encryptor
import json


def init():
    if args_parser.args.mp is None:
        raise AttributeError('Master password must be given')

    init_data = bytes(json.dumps({'init': 'passpass'}), encoding='utf8')

    encryptor.encrypt(args_parser.args.mp, init_data)


init()
