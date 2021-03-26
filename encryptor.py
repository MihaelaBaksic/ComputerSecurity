from Crypto.Cipher import AES
import pbkd


# todo figure out how to store both ct and tag
def encrypt(master_password: str, pt: bytes):
    key = pbkd.derive_encrypt(master_password)
    print("key: ")
    print(key)

    aes = AES.new(key, mode=AES.MODE_EAX)
    nonce = aes.nonce

    f = open('nonce.in', 'wb+')
    f.write(nonce)
    f.close

    ct, tag = aes.encrypt_and_digest(bytes(pt))

    f = open('tag.in', 'wb+')
    f.write(tag)
    f.close()

    f = open('ciphertext.in', 'wb+')
    f.write(ct)
    f.close()

    return ct, tag


def decrypt(master_password: str):
    key = pbkd.derive_decrypt(master_password)
    print("key: ")
    print(key)

    f = open('nonce.in', 'rb')
    nonce = f.read()
    f.close()

    f = open('tag.in', 'rb')
    tag = f.read()
    f.close()

    f = open('ciphertext.in', 'rb')
    ct = f.read()
    f.close()

    aes = AES.new(key, mode=AES.MODE_EAX, nonce=nonce)
    pt = aes.decrypt(ct)
    try:
        aes.verify(tag)
        print("The message is authentic: ", pt)
    except ValueError:
        print("Incorrect master password or database corrupted")


print(encrypt('masterPass', b'plaintext'))
decrypt('masterPass')
