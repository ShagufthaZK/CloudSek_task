#!/usr/bin/env bash
set -e

echo "Waiting for postgres..."

while ! nc -z postgres_db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"
python service/manage.py db init
python service/manage.py db migrate
python service/manage.py db upgrade

python service/run.py