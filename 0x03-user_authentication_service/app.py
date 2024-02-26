#!/usr/bin/env python3
"""
    THis Module Contains a basic flask app
"""
from os import getenv
from flask import Flask, jsonify, abort, request, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def index():
    """ simple index route
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def register_user() -> str:
    """ THis endpoint registers a user
    """
    user_email = request.form.get("email")
    user_password = request.form.get("password")
    try:
        AUTH.register_user(user_email, user_password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": f"{user_email}", "message": "user created"})


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login() -> str:
    """ This endpoint logs a user in
    """
    email = request.form.get("email")
    password = request.form.get("password")
    
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        resp = jsonify({"email": f"{email}", "message": "logged in"})
        resp.set_cookie("session_id", session_id)
        return resp
    abort(401)
    
@app.route("/sessions", methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """ This endpoint logs a user out
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/")
    abort(403)
    
@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """ this endpoint returns a user profile
        when logged in
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": f"{user.email}"}), 200
    abort(403)
    
@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """ this endpoint resets a password 
    """
    email = request.form.get("email")
    if email:
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": f"{email}", "reset_token": f"{token}"}), 200
    abort(403)
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
