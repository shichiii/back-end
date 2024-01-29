#!/bin/bash

python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic

python manage.py runserver 0.0.0.0:8000

# gunicorn Shichi.wsgi:application --bind 0.0.0.0:8000
# gunicorn Shichi.asgi:application --bind 0.0.0.0:8001