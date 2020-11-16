#!/usr/bin/env python3
""" Authentication Module """

import bcrypt


def _hash_password(password: str) -> str:
    """ Returns a salted hash of the input password """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return str(hashed)
