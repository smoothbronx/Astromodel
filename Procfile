release: python manage.py makemigrations --no-input && python manage.py migrate --no-input && python manage.py collectstatic --no-input

web: daphne Astromodel.asgi:asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channel_layer -v2
