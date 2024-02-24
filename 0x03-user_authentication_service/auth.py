#!/usr/bin/env python3
"""
    This Module contains some auth functions
    Author: Peter Ekwere
"""
from db import DB
import bcrypt
from typing import Dict, List
from user import User
from sqlalchemy.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ THis Function converts a password to a hash

    Args:
        password (str): this is the string password

    Returns:
        bytes: this is the returned salt
    """
    password_bytes = bytes(f'{password}', 'utf-8')
    salt = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return salt


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ This method register users

        Args:
            email (str): new user email
            password (str): new user password

        Returns:
            User: a new user object
        """
        user_email = email
        try:
            user = self._db.find_user_by(email=user_email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """ THis method validates a user

        Args:
            email (str): _description_
            password (str): _description_

        Returns:
            bool: _description_
        """
        user_email = email
        try:
            user = self._db.find_user_by(email=user_email)
        except NoResultFound:
            return False
        password_bytes = bytes(f'{password}', 'utf-8')
        if bcrypt.checkpw(password_bytes, user.hashed_password):
            return True
        else:
            return False
