import encryptor
import json
import args_parser


def get():
    if args_parser.args.adr is None:
        raise AttributeError('Address must be given')

    data: str

    try:
        # Get plaintext from database, throws ValueError if validation has failed
        data = str(encryptor.decrypt(args_parser.args.mp).decode('utf-8'))
    except ValueError:
        print("Incorrect master password or database corrupted")
        return

    data_json = json.loads(data)

    try:
        # Get password value for the requested address key
        # Throws KeyError if address doesn't exist
        password = data_json[args_parser.args.adr]
        print('Address: ' + args_parser.args.adr + ' password: ' + password)
    except KeyError:
        print('No password for address ' + args_parser.args.adr)


try:
    get()
except AttributeError as err:
    print(err)
