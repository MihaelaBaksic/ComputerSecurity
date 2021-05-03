from getpass import getpass
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256


# Calculates hash for given password and optional salt
# If salt is not provided the new salt is generated and returned with password hash
def calculate_hash(password: str, salt=None):

    if salt is None:
        salt = str(get_random_bytes(32))

    pass_hash = SHA256.new(bytes(password + salt, encoding='utf-8')).hexdigest()

    return pass_hash, salt
