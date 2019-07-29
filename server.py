#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)
from app import app

if __name__ == "__main__":
    app.run(host='127.0.0.1:5000')
