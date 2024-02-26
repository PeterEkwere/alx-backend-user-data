#!/usr/bin/env python3
"""
    This Module contains some auth functions
    Author: Peter Ekwere
"""
from db import DB
import bcrypt
from typing import Dict, List, Union
from user import User
from sqlalchemy.exc import NoResultFound
from uuid import uuid4


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


def _generate_uuid() -> str:
    """ returns a UUID in string repr
    """
    return str(uuid4())


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

    def create_session(self, email: str) -> str:
        """ This method return the session id
        """
        user_email = email
        try:
            user = self._db.find_user_by(email=user_email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """ This method gets a user using the session id

        Args:
            session_id (str): _description_

        Returns:
            Union[User, None]: _description_
        """
        if session_id:
            try:
                user = self._db.find_user_by(session_id=session_id)
            except NoResultFound:
                return None
            return user
        return None

    def destroy_session(self, user_id: int):
        """ destroys a user session id

        Args:
            user_id (int): _description_
        """
        if user_id:
            try:
                user = self._db.find_user_by(id=user_id)
            except NoResultFound:
                return None
            self._db.update_user(user.id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """ This method is used for resetting a users password

        Args:
            email (str): _description_

        Returns:
            str: _description_
        """
        user = self._db.find_user_by(email=email)
        if user:
            user.reset_token = _generate_uuid()
            return user.reset_token
        raise ValueError

    def update_password(self, reset_token: str, password: str):
        """ This method updates a users password
        """
        user = self._db.find_user_by(reset_token=reset_token)
        if user:
            hashed_password = _hash_password(password)
            user.hashed_password = hashed_password
            user.reset_token = None
        raise ValueError
