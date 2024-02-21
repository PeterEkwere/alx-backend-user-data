#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ This is the login route for session auth 

    Args:
        request (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({ "error": "email missing" }), 400
    if not password:
        return jsonify({ "error": "password missing" }), 400
    user = User.search({'email': email})
    if not user:
        return jsonify({ 'error': 'no user found for this email'}), 404
    user = user[0]
    if not user.is_valid_password(password):
        return jsonify({ "error": "wrong password" }), 401
    if user:
        from api.v1.app import auth
        session_id = auth.create_session(user.id)
        resp = jsonify(user.to_json())
        resp.set_cookie(getenv("SESSION_NAME"), session_id)
        return resp
