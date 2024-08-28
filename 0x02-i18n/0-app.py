#!/usr/bin/env python3
"""A basic flask app that outputs hello world"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    """the index route"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)