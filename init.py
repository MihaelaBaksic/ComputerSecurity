import args_parser
import pbkd
from Crypto.Random import get_random_bytes


def init():
    if args_parser.args.mp is None:
        raise AttributeError('Master password must be given')

    key = pbkd.derive_encrypt(args_parser.args.mp)

    dummy_address = str(get_random_bytes(16))
    dummy_password = str(get_random_bytes(16))








