#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound, InvalidRequestError
from user import Base, User
from typing import Dict, List


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ This method takes an email and hashed_password
        And returns a user object

        Args:
            email (str): This is a user's email
            hashed_password (str): This is a user's hashed password

        Returns:
            User: THis is the created user object
        """
        new_user = User()
        new_user.email = email
        new_user.hashed_password = hashed_password
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwd: Dict) -> User:
        """ THis method finds users by keyworded arguments

        Returns:
            User: _description_
        """
        try:
            user = self._session.query(User).filter_by(**kwd).one()
        except NoResultFound:
            raise NoResultFound()
        except InvalidRequestError:
            raise InvalidRequestError()
        return user

    def update_user(self, user_id: int, **kwd: Dict):
        """ THis method updates a user

        Args:
            user_id (int): this is the user id
        """
        user = self.find_user_by(id=user_id)
        if user_id != user.id:
            raise ValueError
        for key, value in kwd.items():
            setattr(user, key, value)
        self._session.commit()
