from Crypto.Protocol.KDF import scrypt
import Crypto.Random

key_len = 32
N = 2 ** 20
r = 8
p = 1


# Generates and stores salt
# Derives key for 256b AES from master password
def derive_for_encryption(master_password: str):
    salt = Crypto.Random.get_random_bytes(16)
    # save salt for decryption
    f = open('salt.in', 'wb+')
    f.write(salt)
    f.close()

    key = scrypt(master_password, str(salt), key_len, N, r, p)
    return key


# Loads the stored salt
# Derives key for 256b AES from master password
def derive_for_decryption(master_password: str):
    f = open('salt.in', 'rb')
    salt = f.read()
    f.close()

    key = scrypt(master_password, str(salt), key_len, N, r, p)
    return key
