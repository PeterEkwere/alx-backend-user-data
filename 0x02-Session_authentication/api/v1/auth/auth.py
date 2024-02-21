#!/usr/bin/env python3
"""
    This module will contain the auth class
    Author: Peteer Ekwere
"""
from flask import request
from typing import List, TypeVar
from os import getenv


session_id = getenv('SESSION_NAME')


class Auth:
    """ This is the authentication class
    """

    def __init__(self) -> None:
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """

        Args:
            path (str): _description_
            excluded_paths (List[str]): _description_

        Returns:
            bool: _description_
        """
        if path and path[-1] != "/":
            path = path + "/"
        if path is None:
            return True
        if excluded_paths is None:
            return True
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        """
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        """
        return None

    def session_cookie(self, request=None):
        """ This Method returns a cookie value from a request

        Args:
            request (_type_, optional): _description_. Defaults to None.
        """
        if request:
            cookie_value = request.cookies.get(session_id)
            return cookie_value
        return None
