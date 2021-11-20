#!/usr/bin/env bash
# start-server.sh
echo "Hello from Projet Fingerprinting White Marbles"
echo "starting rabbitmq"
rabbitmq-server > rabbit_mq.log 1>&1 &
echo "starting celery server"
celery -A djangobaseproject worker -l INFO  > celery.log 2>&1 &
python manage.py collectstatic --no-input
if [ -n "$MIGRATE" ] ; then
    (echo "making migrations and running them"
    python manage.py makemigrations --no-input
    python manage.py migrate --no-input)
fi
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (echo "creating superuser ${DJANGO_SUPERUSER_USERNAME}" && python manage.py createsuperuser --no-input --noinput --email 'blank@email.com')
fi
gunicorn djangobaseproject.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3 & nginx -g "daemon off;"