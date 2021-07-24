#!/bin/bash

python manage.py waiting-for-database

python manage.py makemigrations --no-input

python manage.py migrate --no-input

python manage.py collectstatic --no-input

python manage.py runserver 0.0.0.0:$1