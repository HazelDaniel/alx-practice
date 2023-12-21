#!/usr/bin/env python3
"""this module is the practice module for flask"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<p>hello world</p>"


@app.route('/<name>')
def say_name(name):
    return f"<p>hello {escape(name)}</p>"
