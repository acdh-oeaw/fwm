#!/usr/bin/env bash
# start-server.sh
echo "Hello from Projet Fingerprinting White Marbles"
mkdir -p /opt/app/media/images
chown -R www-data:www-data /opt/app/media
chmod -R 755 /opt/app/media
echo "starting rabbitmq"
rabbitmq-server > rabbit_mq.log 1>&1 &
echo "starting celery server"
uv run celery -A djangobaseproject worker -l INFO  > celery.log 2>&1 &
uv run manage.py collectstatic --no-input
uv run manage.py migrate --no-input
uv run gunicorn djangobaseproject.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3 & nginx -g "daemon off;"