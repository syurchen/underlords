#!/usr/bin/env python3
from app import app, routes, models
from flask import Flask

#app.config.from_pyfile('config/main.cfg')

app.static_folder = app.config['STATIC_FOLDER']

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
