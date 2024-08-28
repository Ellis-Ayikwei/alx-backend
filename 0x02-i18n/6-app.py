#!/usr/bin/env python3
"""A basic Flask app that outputs 'Hello, World' with localization support."""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Config class for Flask app settings."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "fr"
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


def get_user():
    """Get the user from the request."""
    login_as = request.args.get('login_as')
    if not login_as:
        return None
    userId = int(login_as)
    print(userId)
    return users.get(userId)


@babel.localeselector
def get_locale():
    """Get the best match locale from the request."""
    # Check if locale is in the request arguments
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale

    user = g.user
    if user and user.get('locale') in Config.LANGUAGES:
        return user.get('locale')

    # If no locale is found, check the Accept-Language header
    if request.accept_languages:
        return request.accept_languages.best_match(Config.LANGUAGES)

    # Default to the app's default locale
    return app.config['LANGUAGES']


@app.before_request
def before_request():
    """Execute before each request."""
    g.user = get_user()


@app.route("/")
def index_route():
    """Render the index template."""
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(debug=True)
