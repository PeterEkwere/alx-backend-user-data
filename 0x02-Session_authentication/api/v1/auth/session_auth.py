#!/usr/bin/env python3
"""
    This module will contain the auth class
    Author: Peter Ekwere
"""
from flask import request, jsonify
import base64
from uuid import uuid4
from models.user import User
from typing import List, TypeVar
from api.v1.auth.auth import Auth
    

class SessionAuth(Auth):
    """ This is the Session Authentication class
    """
    user_id_by_session_id = {}

    def __init__(self) -> None:
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
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
        """ This method returns a user based on a cookie value

        Args:
            request (_type_, optional): this is the request. Defaults to None.
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)
