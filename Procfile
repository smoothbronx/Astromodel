release: cd Astromodel/ && python manage.py waiting-for-database && python manage.py makemigrations --no-input && python manage.py migrate --no-input && python manage.py collectstatic --no-input && python manage.py initialize-admin
web: cd Astromodel/ && daphne Astromodel.asgi:application --port $PORT --bind 0.0.0.0 -v2
