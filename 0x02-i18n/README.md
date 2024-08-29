# 0x02. i18n (Internationalization)

This project focuses on implementing internationalization (i18n) in a Flask web application, allowing it to support multiple languages and time zones.

## Learning Objectives

By the end of this project, you should be able to:
- Parametrize Flask templates to display different languages.
- Infer the correct locale based on URL parameters, user settings, or request headers.
- Localize timestamps according to the user's timezone.

## Requirements

- All files are written in Python 3.7 and are compatible with Ubuntu 18.04 LTS.
- Code follows `pycodestyle` style (version 2.5).
- All files must be executable and end with a new line.
- Modules, classes, and functions should have descriptive docstrings.
- All functions should be type annotated.

## Project Structure

- `0-app.py`: Basic Flask app setup.
- `1-app.py`: Setup Flask-Babel with basic configuration.
- `2-app.py`: Determine locale from request.
- `3-app.py`: Parametrize templates using the `_` or `gettext` function.
- `4-app.py`: Implement locale switching using URL parameters.
- `5-app.py`: Mock user login and personalize content.
- `6-app.py`: Use user locale settings for language selection.
- `7-app.py`: Infer and validate the appropriate timezone.
- `app.py`: Final app combining all the features.
- `babel.cfg`: Babel configuration file.
- `templates/`: Contains HTML templates.
- `translations/`: Contains translations for supported languages.

## Tasks

### 0. Basic Flask App
Set up a basic Flask app with a single `/` route and an `index.html` template that displays "Welcome to Holberton" as the page title and "Hello world" as the header.

### 1. Basic Babel Setup
Install Flask-Babel, configure the available languages (`en`, `fr`), and set the default locale and timezone.

### 2. Get Locale from Request
Create a `get_locale` function to determine the best match for the supported languages based on the `Accept-Language` header.

### 3. Parametrize Templates
Use the `_` or `gettext` function to parametrize your templates. Initialize and compile translation files for English and French.

### 4. Force Locale with URL Parameter
Implement the ability to force a particular locale by passing the `locale` parameter in the URL. Adjust the `get_locale` function accordingly.

### 5. Mock Logging In
Create a mock user login system using URL parameters. Display personalized content based on whether a user is logged in.

### 6. Use User Locale
Update the `get_locale` function to prioritize the user's preferred locale, if available.

### 7. Infer Appropriate Time Zone
Implement a `get_timezone` function to infer the appropriate timezone, allowing overrides through URL parameters and user settings.

### 8. Display the Current Time (Advanced)
Display the current time on the home page based on the inferred timezone. Ensure the time is formatted according to the selected locale.

## Installation

To install the necessary dependencies, run:
```bash
pip3 install -r requirements.txt
