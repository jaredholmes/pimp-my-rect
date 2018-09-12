# Pimp My Rect

A rectangle customization single page application for Xfive built using Vue, Bootstrap and Django.

## Getting Started

Clone this repo and cd into the directory.
```bash
cd jaredholmes-js-test
```

Install [Pipenv](https://github.com/pypa/pipenv) using pip.
```bash
pip install pipenv
```

Or intsall pipenv using [Homebrew](https://brew.sh).
```bash
brew install pipenv
```

Spawn the virtual environment and install the Python dependencies.
```bash
pipenv shell
pipenv install
```

Make the database migrations.
```python
python manage.py migrate
```

Startup the server.
```python
python manage.py runserver
```

Visit relevant localhost port in your browser (most likely http://localhost:8000/), and you should be good to go.

### Navigating files

The files are laid out in the typical Django format. Below are the locations of some of the files you may want to take a look at:
* **HTML files:** pmr_app/templates/pmr_app/
* **Front-end files (JS, Vue, Webpack config, etc.):** pmr_app/static/pmr_app/
* **Views:** pmr_app/views.py
* **URL conf:** pmr_app/urls.py
* **Models:** pmr_app/models.py

### Usage

Simply sign up and create, view and delete your rectangles.
