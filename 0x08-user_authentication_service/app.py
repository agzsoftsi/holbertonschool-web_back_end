#!/usr/bin/env python3

from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from flask import redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def hello_world() -> str:
    msg = {"message": "Bienvenue"}
    return jsonify(msg)


@app.route('/users', methods=['POST'])
def register_user() -> str:

    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    msg = {"email": email, "message": "user created"}
    return jsonify(msg)


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /sessions
    Creates new session for user, stores as cookie
    Email and pswd fields in x-www-form-urlencoded request
    Return:
      - JSON payload
    """
    form_data = request.form

    if "email" not in form_data:
        return jsonify({"message": "email required"}), 400
    elif "password" not in form_data:
        return jsonify({"message": "password required"}), 400
    else:

        email = request.form.get("email")
        pswd = request.form.get("password")

        if AUTH.valid_login(email, pswd) is False:
            abort(401)
        else:
            session_id = AUTH.create_session(email)
            response = jsonify({
                "email": email,
                "message": "logged in"
                })
            response.set_cookie('session_id', session_id)

            return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def log_out() -> None:
    """Find the user with the requested session ID.
    If the user exists destroy the session and redirect the user to GET /.
    If the user does not exist, respond with a 403 HTTP status.
    """
    session_id = request.cookies.get("session_id", None)

    if session_id is None:
        abort(400)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)

    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
