release: python manage.py makemigrations --no-input && python manage.py migrate --no-input && python manage.py collectstatic --no-input

web: gunicorn Astromodel.wsgi --log-file -
