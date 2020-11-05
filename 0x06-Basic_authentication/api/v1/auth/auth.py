#!/usr/bin/env python3
""" Module of Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for requiring authentication """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        l_path = len(path)
        slash_path = True if path[l_path - 1] == '/' else False
        for exc in excluded_paths:
            l_exc = len(exc)
            slash_exc = True if exc[l_exc - 1] == '/' else False

            if slash_path and not slash_exc:
                path = path[:-1]
            elif not slash_path and slash_exc:
                path += '/'

            if path == exc:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method that handles authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Validates current user """
        return None
