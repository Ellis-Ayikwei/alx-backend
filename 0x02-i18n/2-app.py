#!/usr/bin/env python3
"""A basic Flask app that outputs 'Hello, World' with localization support."""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config class for Flask app settings."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@babel.localeselector
def get_locale():
    """Get the best match locale from the request."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route("/")
def index():
    """The index route."""
    return render_template("2-index.html")


if __name__ == "__main__":
     app.run(host="0.0.0.0", port="5000", debug=True)
