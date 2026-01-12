[![Linting](https://github.com/acdh-oeaw/fwm/actions/workflows/lint.yml/badge.svg)](https://github.com/acdh-oeaw/fwm/actions/workflows/lint.yml)
[![Test](https://github.com/acdh-oeaw/fwm/actions/workflows/test.yml/badge.svg)](https://github.com/acdh-oeaw/fwm/actions/workflows/test.yml)

# Fingerprinting White Marbles

Web-Application for the FWF-Project "Fingerprinting White Marbles" [(P 33042)](https://pf.fwf.ac.at/de/wissenschaft-konkret/project-finder/48544)

## install

> [!NOTE]  
> This project uses [uv](https://docs.astral.sh/uv/) to manage dependencies. See [uv-docs](https://docs.astral.sh/uv/getting-started/installation/) on how to install it.

* clone the repo `git clone https://github.com/acdh-oeaw/fwm.git`
* change into the project's root directory e.g. `cd fwm`
* create a Postgresql database `fwm` and install postgis extension
* expose environment variables from `default.env` (adapt if necessary, see `djangobaseproject/settings.py`)
  ```shell
  source ./export_env_variables.sh
  ```
* run migrations `python manage.py migrate`
* start the dev sever `python manage.py runserver`
* go to [http://127.0.0.1:8000](http://127.0.0.1:8000/) and check if everything works

### celery

To use celery task manager you'll need to
* have rabbit-mq installed and running
    ```shell
    sudo apt install rabbitmq-server
    sudo systemctl stop rabbitmq-server
    ```
* [to start run `sudo systemctl stop rabbitmq-server`]
* start celery
    ```shell
    uv run celery -A djangobaseproject worker -l INFO
    ```

### linting and testing

### run tests
```shell
uv run coverage run ./manage.py test -v 2
```

### check linting
```shell
ruff check .
```

### fix linting
```shell
ruff format .
```

## Images
Images from Axiell are stored on disk. There is a dedicated management-command to download all images
```shell
uv run manage.py populate_streams
```

You can also delete all images (and remove the matching database entries), you can run
```shell
uv run manage.py delete_streams
```
This might become necessary if you somehow deleted (some) images on disk but kept the databse entries

## DB-config

configuration of database settings (and debug mode) is done via env variables, see `djangobaseproject/settings.py` which variables can be set

## running async tasks

In order to run async task, you'll need to start a celery worker e.g. with
* `uv run celery -A djangobaseproject worker -l INFO`

## Docker

At the ACDH-CH we use a centralized database-server. So instead of spawning a database for each service our services are talking to a database on this centralized db-server. This setup is reflected in the dockerized setting as well, meaning it expects an already existing database (either on your host, e.g. accessible via 'localhost' or some remote one)

### building the image

```shell
docker build -t fwm:latest .
```

### running the image

To run the image you should provide an `.env` file to pass in needed environment variables; see example below:

```shell
docker run -it -p 8020:8020 --network="host" --rm --env-file default.env --name fwm fwm:latest
```

-----

This project was bootstraped by [djangobase-cookiecutter](https://github.com/acdh-oeaw/djangobase-cookiecutter)
