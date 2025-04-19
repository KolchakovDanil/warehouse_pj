#!/bin/bash


until mysqladmin ping -h"db" -u root -p"$MYSQL_ROOT_PASSWORD"; do
  echo "Waiting for MySQL to start..."
  sleep 5
done

echo "MySQL is up and running!"


python manage.py migrate --no-input
python manage.py collectstatic --noinput

exec "$@"
