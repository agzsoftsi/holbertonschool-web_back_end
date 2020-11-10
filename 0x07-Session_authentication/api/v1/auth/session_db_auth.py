#!/usr/bin/env python3
''' Define SessionDBAuth class. '''

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    ''' Extend behavior of SessionExpAuth for database session storage. '''

    def create_session(self, user_id=None):
        ''' Create and store session. '''
        if user_id is None:
            return None

        # Get session ID from parent class method
        session_id = super().create_session(user_id)

        # Create and save instance of UserSession with user ID and session ID
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()

        return session_id

    def user_id_for_session_id(self, session_id=None):
        ''' Return user ID associated with given session ID. '''
        if session_id is None:
            return None

        found_user = UserSession.search({'session_id': session_id})
        if not found_user:
            return None

        found_user = found_user[0]

        if self.session_duration <= 0:
            return found_user.user_id

        # Check if session has expired
        creation_time = found_user.created_at

        session_length = timedelta(seconds=self.session_duration)

        expiry_time = creation_time + session_length

        if expiry_time < datetime.utcnow():
            return None
        return found_user.user_id

    def destroy_session(self, request=None):
        ''' Destroy session associated with request. '''
        # Get session ID from request cookie
        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        # Get user ID associated with session ID
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        # Remove session record from file
        found_user = UserSession.search({'session_id': session_id})
        if not found_user:
            return False

        found_user = found_user[0]
        found_user.remove()
        return True
