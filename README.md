[![Linting](https://github.com/acdh-oeaw/fwm/actions/workflows/lint.yml/badge.svg)](https://github.com/acdh-oeaw/fwm/actions/workflows/lint.yml)

# Fingerprinting White Marbles

Web-Application for the FWF-Project "Fingerprinting White Marbles" [(P 33042)](https://pf.fwf.ac.at/de/wissenschaft-konkret/project-finder/48544)

## install

> [!NOTE]  
> This project uses [uv](https://docs.astral.sh/uv/) to manage dependencies. See [uv-docs](https://docs.astral.sh/uv/getting-started/installation/) on how to install it.

* clone the repo `git clone https://github.com/acdh-oeaw/fwm.git`
* change into the project's root directory e.g. `cd fwm`
* run migrations `python manage.py migrate`
* start the dev sever `python manage.py runserver`
* go to [http://127.0.0.1:8000](http://127.0.0.1:8000/) and check if everything works

## DB-config

configuration of database settings (and debug mode) is done via env variables, see `djangobaseproject/settings.py` which variables can be set

## running async tasks

In order to run async task, you'll need to start a celery worker e.g. with
* `uv run celery -A djangobaseproject worker -l INFO`


## Docker

At the ACDH-CH we use a centralized database-server. So instead of spawning a database for each service our services are talking to a database on this centralized db-server. This setup is reflected in the dockerized setting as well, meaning it expects an already existing database (either on your host, e.g. accessible via 'localhost' or some remote one)

### building the image

* `docker build -t fwm:latest .`
* `docker build -t fwm:latest --no-cache .`


### running the image

To run the image you should provide an `.env` file to pass in needed environment variables; see example below:

* `docker run -it -p 8020:8020 --env-file env.default --name fwm fwm:latest`

-----

This project was bootstraped by [djangobase-cookiecutter](https://github.com/acdh-oeaw/djangobase-cookiecutter)
