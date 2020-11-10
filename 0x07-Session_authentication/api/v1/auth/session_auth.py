#!/usr/bin/env python3
''' Define SessionAuth class. '''

from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    ''' Extend behavior of Auth class for session authentication. '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        ''' Create and return a session ID for a user ID. '''
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id

        return session_id
