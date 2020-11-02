#!/usr/bin/env python3
'''
   5. Encrypting passwords
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
