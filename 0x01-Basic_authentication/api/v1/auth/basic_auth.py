#!/usr/bin/env python3
"""
    This module will contain the auth class
    Author: Peteer Ekwere
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth

class BasicAuth(Auth):
    """ This is the BasicAuthentication class
    """

    def __init__(self) -> None:
        super().__init__()
