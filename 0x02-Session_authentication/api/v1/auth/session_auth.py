#!/usr/bin/env python3
"""
    This module will contain the auth class
    Author: Peter Ekwere
"""
from flask import request
import base64
from models.user import User
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ This is the Session Authentication class
    """

    def __init__(self) -> None:
        super().__init__()