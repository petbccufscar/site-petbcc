#!/bin/sh
set -e

echo "Starting entrypoint..."

# Aplica migrations
python manage.py migrate

if [ "$DEBUG" = "1" ]; then
    echo "Running in DEV mode..."
    # O tailwind já está sendo gerenciado pelo outro container, 
    # então aqui apenas iniciamos o servidor.
    exec python manage.py runserver 0.0.0.0:8000
else
    echo "Running in PROD mode..."
    python manage.py tailwind build
    python manage.py collectstatic --noinput
    exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3
fi