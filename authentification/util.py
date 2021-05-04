from getpass import getpass
import re
import argon2

t_cost = 16
parallelism = 2
hash_len = 32
salt_len = 16


# Calculates hash for given password and optional salt
# If salt is not provided the new salt is generated and returned with password hash
def calculate_hash(password: str):

    a2_hasher = argon2.PasswordHasher(time_cost=t_cost, parallelism=parallelism, hash_len=hash_len, salt_len=salt_len)
    pass_hash = a2_hasher.hash(password)
    return pass_hash


def verify_hash(_hash: str, password: str):
    a2_hasher = argon2.PasswordHasher(time_cost=t_cost, parallelism=parallelism, hash_len=hash_len, salt_len=salt_len)
    a2_hasher.verify(_hash, password)


def get_password(prompt: str):
    password = getpass(prompt)
    passwordRepeated = getpass("Repeat " + prompt.lower())
    return password == passwordRepeated, password


def validate_password(password: str):
    min_len = 8

    if len(password) < min_len\
            or not bool(re.search(r'\d', password))\
            or not bool(re.match(r'\w*[A-Z]\w', password)):
        return False

    return True

