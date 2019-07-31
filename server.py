#!/usr/bin/env python3
from app.config.main import Config
from flask import Flask
from app import app, routes

#app.config.from_pyfile('config/main.cfg')

app.config.from_object(Config())
app.static_folder = app.config['STATIC_FOLDER']


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
