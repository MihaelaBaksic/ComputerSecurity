import encryptor
import json
import args_parser


def get():
    if args_parser.args.mp is None:
        raise AttributeError('Master password must be given')
    if args_parser.args.adr is None:
        raise AttributeError('Address must be given')

    data: str

    try:
        data = str(encryptor.decrypt(args_parser.args.mp).decode('utf-8'))
    except ValueError:
        print("Incorrect master password or database corrupted")
        return

    data_json = json.loads(data)

    try:
        password = data_json[args_parser.args.adr]
        print('Address: ' + args_parser.args.adr + ' password: ' + password)
    except KeyError:
        print('No password for address ' + args_parser.args.adr)


get()
