#!/usr/bin/env python3
from app import app, routes
from flask import Flask

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
