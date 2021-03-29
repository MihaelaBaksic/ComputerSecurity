from Crypto.Cipher import AES
import pbkd


def encrypt(master_password: str, pt: bytes):
    key = pbkd.derive_for_encryption(master_password)

    aes = AES.new(key, mode=AES.MODE_EAX)

    ct, tag = aes.encrypt_and_digest(pt)

    f = open('db.bin', 'wb+')
    f.write(aes.nonce)
    f.write(tag)
    f.write(ct)
    f.close

    # f = open('tag.in', 'wb+')
    # f.write(tag)
    # f.close()

    # f = open('ciphertext.in', 'wb+')
    # f.write(ct)
    # f.close()


def decrypt(master_password: str):
    key = pbkd.derive_for_decryption(master_password)

    f = open('db.bin', 'rb')
    nonce = f.read(16)
    tag = f.read(16)
    ct = f.read()
    f.close()

    # f = open('tag.in', 'rb')
    # tag = f.read()
    # f.close()

    # f = open('ciphertext.in', 'rb')
    # ct = f.read()
    # f.close()

    aes = AES.new(key, mode=AES.MODE_EAX, nonce=nonce)
    pt = aes.decrypt(ct)

    aes.verify(tag)
    return pt

# encrypt('masterPass', b'plaintext'))
# decrypt('masterPass')
