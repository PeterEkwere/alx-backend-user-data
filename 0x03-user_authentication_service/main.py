#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'peter@gmail.com'
password = 'ABCD'
auth = Auth()

auth.register_user(email, password)

print(auth.valid_login(email, password))

print(auth.valid_login(email, "EFGH"))

print(auth.valid_login("IJKL@email.com", password))
