#!/usr/bin/env python3
"""
    This Module contains some auth functions
    Author: Peter Ekwere
"""
import bcrypt


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
