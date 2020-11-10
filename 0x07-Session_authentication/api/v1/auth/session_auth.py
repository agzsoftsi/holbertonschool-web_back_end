#!/usr/bin/env python3
''' Define SessionAuth class. '''

from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        ''' Return user ID associated with specified session ID. '''
        if session_id is None or not isinstance(session_id, str):
            return None

        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        ''' Returns a User instance based on a cookie value '''

        session_id = self.session_cookie(request)
        # print(session_id)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        # print(user_id)

        return User.get(user_id)

    def destroy_session(self, request=None):
        """Deletes de user session / logout"""

        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)

        if not user_id:
            return False

        try:
            del self.user_id_by_session_id[session_id]
        except Exception:
            pass

        return True
