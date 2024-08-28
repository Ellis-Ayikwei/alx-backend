#!/usr/bin/env python3
"""A basic Flask app that outputs 'Hello, World' with localization support."""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Config class for Flask app settings."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

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


def get_user():
    login_as = request.args.get('login_as')
    if not login_as:
        return None
    userId = int(login_as)
    print(userId)
    return users.get(userId)


@app.before_request
def before_request():
    g.user = get_user()


@app.route("/")
def index_route():
    """Render the index template."""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)
