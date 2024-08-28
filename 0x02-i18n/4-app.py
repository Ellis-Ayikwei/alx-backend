#!/usr/bin/env python3
"""A basic Flask app that outputs 'Hello, World' with localization support."""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config class for Flask app settings."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get the best match locale from the request."""
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def index_route():
    """Render the index template."""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
