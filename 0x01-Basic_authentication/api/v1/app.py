#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from api.v1.auth.auth import Auth


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
auth_type = os.getenv("AUTH_TYPE")
none_paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']


if auth_type == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()
elif auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()


@app.before_request
def authenticate():
    """ This method filters each request

    Returns:
        _type_: _description_
    """
    if auth:
        if auth.require_auth(request.path, none_paths):
            if auth.authorization_header(request):
                abort(401)
            if auth.current_user(request) is None:
                abort(403)
    return


@app.errorhandler(403)
def not_found_403(error):
    """ not found error for 403
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(401)
def not_found_401(error):
    """ not found error for 401
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
