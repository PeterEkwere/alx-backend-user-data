#!/usr/bin/env python3
"""
    This module will contain the auth class
    Author: Peteer Ekwere
"""
from flask import request
from typing import List, TypeVar


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
        if "Authorization" not in request:
            return None
        return request['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        """
        return None
