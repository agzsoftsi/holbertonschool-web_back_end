#!/usr/bin/env python3
""" Authentication Module """

from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> str:
    """ Returns a salted hash of the input password """
    return hashpw(password.encode('utf-8'), gensalt())
