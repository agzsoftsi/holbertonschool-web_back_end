#!/usr/bin/env python3
""" Module of Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for requiring authentication """
        return False

    def authorization_header(self, request=None) -> str:
        """ Method that handles authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Validates current user """
        return None
