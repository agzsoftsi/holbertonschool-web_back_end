#!/usr/bin/env python3

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world() -> str:
    msg = {"message": "Bienvenue"}
    return jsonify(msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
