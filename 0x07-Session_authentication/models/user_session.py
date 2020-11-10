#!/usr/bin/env python3
''' Define UserSession class. '''

from models.base import Base


class UserSession(Base):
    ''' Extend behaviors of Base class for session authentication using a DB.
    '''

    def __init__(self, *args: list, **kwargs: dict):
        ''' Initialize class instance. '''
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
