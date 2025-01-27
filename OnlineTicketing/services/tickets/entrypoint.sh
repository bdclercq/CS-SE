#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z tickets-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

python -u manage.py run -h 0.0.0.0 -p 5004
