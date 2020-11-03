#!/usr/bin/env python3
'''
   5. Encrypting passwords
   6. Check valid password
'''
import bcrypt


def hash_password(password: str) -> bytes:
    ''' Description: Implement a hash_password function that expects one string
                     argument name password and returns a salted, hashed
                     password, which is a byte string.

        Use the bcrypt package to perform the hashing (with hashpw).
    '''
    pass_encoded = password.encode()
    pass_hashed = bcrypt.hashpw(pass_encoded, bcrypt.gensalt())

    return pass_hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
       Description: Implement an is_valid function that expects 2 arguments and
                    returns a boolean.

       Arguments:   hashed_password: bytes type
                    password: string type
       Use bcrypt to validate that the provided password matches the hashed
       password.
    '''
    valid = False
    pass_encoded = password.encode()
    if bcrypt.checkpw(pass_encoded, hashed_password):
        valid = True
    return valid
