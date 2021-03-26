from Crypto.Protocol.KDF import scrypt
import Crypto.Random


def derive_for_encryption(master_password: str):
    # todo define salt length
    salt = Crypto.Random.get_random_bytes(16)
    # save salt for decryption
    f = open('salt.in', 'wb+')
    f.write(salt)
    f.close()

    key = scrypt(master_password, str(salt), 32, 2 ** 20, 8, 1)
    return key


def derive_for_decryption(master_password: str):
    f = open('salt.in', 'rb')
    salt = f.read()
    f.close()

    key = scrypt(master_password, str(salt), 32, 2 ** 20, 8, 1)
    return key

# print(derive_encrypt('masterPass'))
