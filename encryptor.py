from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import pbkd

# todo figure out how to store both ct and tag
def encrypt(master_password: str, data: str):
    iv = get_random_bytes(16)
    f = open('vector.in', 'wb+')
    f.write(iv)
    f.close

    key = pbkd.derive_encrypt(master_password)
    aes = AES.new(key, mode=AES.MODE_CBC, iv=iv)

    ct, tag = aes.encrypt_and_digest(data)

    f = open('data.crypto', 'wb+')
    f.write(tag)
    f.close()

# todo
def decrypt(master_password: str, data: str):
    f = open('vector.in', 'rb')
    iv = f.read()
    f.close()

    key = pbkd.derive_decrypt(master_password)
