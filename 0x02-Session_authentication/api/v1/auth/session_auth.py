#!/usr/bin/env python3
"""
<<<<<<< HEAD
    This module will contain the auth class
    Author: Peter Ekwere
"""
from flask import request, jsonify
import base64
from uuid import uuid4
from models.user import User
from typing import List, TypeVar
=======
    This module contains the SessionAuth class
    Author: Peter Ekwere
"""
>>>>>>> 75a0718aa89870003da1ac4471c0d017d79da968
from api.v1.auth.auth import Auth
    

class SessionAuth(Auth):
<<<<<<< HEAD
    """ This is the Session Authentication class
    """
=======
    """
    This is the SessionAuth class.
    """

>>>>>>> 75a0718aa89870003da1ac4471c0d017d79da968
    user_id_by_session_id = {}

    def __init__(self) -> None:
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
<<<<<<< HEAD
        """ this method creates a session id

        Args:
            user_id (str, optional): This is the users id. Defaults to None.

        Returns:
            str: returns a session id
        """
        if user_id and isinstance(user_id, str):
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ This Method returns a user id based on a session id
=======
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
>>>>>>> 75a0718aa89870003da1ac4471c0d017d79da968

        Args:
            session_id (str, optional): this is the session id.
            Defaults to None.

        Returns:
            str: returns the user id
        """
        if session_id and isinstance(session_id, str):
            return self.user_id_by_session_id.get(session_id)
        return None
    
    def current_user(self, request=None):
<<<<<<< HEAD
        """ This method returns a user based on a cookie value
=======
        """ THis method retrieves a User instance based on the cookies
        """
        from models.user import User
>>>>>>> 75a0718aa89870003da1ac4471c0d017d79da968

        Args:
            request (_type_, optional): this is the request. Defaults to None.
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)
<<<<<<< HEAD
=======

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
>>>>>>> 75a0718aa89870003da1ac4471c0d017d79da968
