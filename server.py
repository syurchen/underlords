#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)
from app import app
app.config.from_object('app.config.main')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
