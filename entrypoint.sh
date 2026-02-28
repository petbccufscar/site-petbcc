#!/bin/sh
set -e

echo "Starting entrypoint..."

# aplica migrations
python manage.py migrate

# se DEV (DEBUG=1)
if [ "$DEBUG" = "1" ]; then
    echo "Running in DEV mode..."
    python manage.py tailwind install
    python manage.py tailwind build
    python manage.py tailwind start &
    exec python manage.py runserver 0.0.0.0:8000
else
    echo "Running in PROD mode..."
    python manage.py collectstatic --noinput
    exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3
fi