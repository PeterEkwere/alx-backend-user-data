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
def register_user():
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
def login():
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
def logout():
    """ This endpoint logs a user out
    """
    session_id = request.form.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/")
    abort(403)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
