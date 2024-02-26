#!/usr/bin/env python3
"""
Main file
"""
import requests
EMAIL = "Peterekwere007@gmail.com"
PASSWD = "1122"
NEW_PASSWD = "t4rt1fl3tt3"


def register_user(email: str, password: str) -> None:
    payload = {f'email={email}', f'password={password}'}
    url = "localhost:5000/users"
    requests.get(url, params=payload)


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
"""    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)"""
