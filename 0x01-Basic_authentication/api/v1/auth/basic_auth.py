#!/usr/bin/env python3
"""
    This module will contain the auth class
    Author: Peter Ekwere
"""
from flask import request
import base64
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ This is the BasicAuthentication class
    """

    def __init__(self) -> None:
        super().__init__()

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ This Method  returns the Base64 part of the Authorization header

        Args:
            authorization_header (str): authorization header

        Returns:
            str:
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        split = authorization_header.split()
        if len(split) < 2:
            return None
        stat = split[0]
        auth = split[1]

        if stat != 'Basic':
            return None
        return auth

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ This Method returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_byte = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_byte.decode('utf-8')
            return decoded_str
        except BaseException:
            return None
