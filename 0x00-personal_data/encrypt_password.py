#!/usr/bin/env python3
"""
    THis module contains functions for hashing passwords
    Author: Peter Ekwere
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ THis Function converts a password to a hash

    Args:
        password (str): this is the string password

    Returns:
        bytes: this is the returned salt
    """
    password_bytes = bytes(f'{password}', 'utf-8')
    salt = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return salt


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ THis function checks if the password is correct
    """
    password_bytes = bytes(f'{password}', 'utf-8')
    if bcrypt.checkpw(password_bytes, hashed_password):
        return True
    else:
        return False
