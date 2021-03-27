import args_parser
import encryptor
import json


def put():
    if args_parser.args.adr is None:
        raise AttributeError('Address must be given')
    if args_parser.args.pwd is None:
        raise AttributeError('Address password must be given')

    data: str

    try:
        data = str(encryptor.decrypt(args_parser.args.mp).decode('utf-8'))
    except ValueError:
        print("Incorrect master password or database corrupted")
        return

    data_json = json.loads(data)

    data_json[args_parser.args.adr] = args_parser.args.pwd

    encryptor.encrypt(args_parser.args.mp, bytes(json.dumps(data_json), encoding='utf8'))


try:
    put()
    print("Stored password for address " + args_parser.args.adr)
except AttributeError as err:
    print(err)
