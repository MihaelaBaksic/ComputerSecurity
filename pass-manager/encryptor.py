from Crypto.Cipher import AES
import pbkd

nonce_len = 16
tag_len = 16


# Encrypts plaintext with master password derived key
# Stores nonce, tag and ciphertext to database
def encrypt(master_password: str, pt: bytes):
    key = pbkd.derive_for_encryption(master_password)

    aes = AES.new(key, mode=AES.MODE_EAX)

    ct, tag = aes.encrypt_and_digest(pt)

    f = open('db.bin', 'wb+')
    f.write(aes.nonce)
    f.write(tag)
    f.write(ct)
    f.close


# Decrypts ciphertext with master password derived key
# Performs tag validation
# Throws ValueError for corrupted database or wrong master password
def decrypt(master_password: str):
    key = pbkd.derive_for_decryption(master_password)

    f = open('db.bin', 'rb')
    nonce = f.read(nonce_len)
    tag = f.read(tag_len)
    ct = f.read()
    f.close()

    aes = AES.new(key, mode=AES.MODE_EAX, nonce=nonce)
    pt = aes.decrypt(ct)
    aes.verify(tag)

    return pt
