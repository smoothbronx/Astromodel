#!/bin/sh

python manage.py waiting-for-database

python manage.py makemigrations --no-input

python manage.py migrate --no-input

python manage.py initialize-admin

python manage.py collectstatic --no-input

exec "$@"