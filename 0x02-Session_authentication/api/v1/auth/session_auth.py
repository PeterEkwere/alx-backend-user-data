#!/usr/bin/env python3
"""
    This module contains the SessionAuth class
    Author: Peter Ekwere
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    This is the SessionAuth class.
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ This Method creates a new session for a user.
        """
        if not user_id or type(user_id) != str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ This method retrieves a user id from the session id
        """
        if not session_id or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None):
        """ THis method retrieves a User instance based on the cookies
        """
        from models.user import User

        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ THis method deletes a user session / logout
        """
        if not request:
            return False
        session_id = self.session_cookie(request)
        if not session_id or not self.user_id_for_session_id(session_id):
            return False
        del self.user_id_by_session_id[session_id]
        return True
