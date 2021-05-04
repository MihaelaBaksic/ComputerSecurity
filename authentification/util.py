from getpass import getpass
import re
import argon2


# Calculates hash for given password and optional salt
# If salt is not provided the new salt is generated and returned with password hash
def calculate_hash(password: str):
    a2_hasher = argon2.PasswordHasher(time_cost=16, parallelism=2, hash_len=32, salt_len=16)
    pass_hash = a2_hasher.hash(password)
    return pass_hash


# Verifies provided hash against the provided password
def verify_hash(_hash: str, password: str):
    a2_hasher = argon2.PasswordHasher(time_cost=16, parallelism=2, hash_len=32, salt_len=16)
    a2_hasher.verify(_hash, password)


# Requests user to enter and repeat a password
def get_password(prompt: str):
    password = getpass(prompt)
    passwordRepeated = getpass("Repeat " + prompt.lower())
    return password == passwordRepeated, password


# Performs validation of provided plaintext password
# Password must be at least 8 characters long,
# contain at least one upper case letter and number
def validate_password_format(password: str):
    min_len = 8

    if len(password) < min_len \
            or not bool(re.search(r'\d', password)) \
            or not bool(re.match(r'\w*[A-Z]\w', password)):
        return False

    return True
