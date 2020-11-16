#!/usr/bin/env python3
""" Authentication Module """

from db import DB
from user import User
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> str:
    """ Returns a salted hash of the input password """
    return hashpw(password.encode('utf-8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Instance """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers and returns a new user if email isn't listed"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except Exception:
            return self._db.add_user(email, _hash_password(password))
