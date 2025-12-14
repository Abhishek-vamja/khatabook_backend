#!/bin/bash
cd /home/ec2-user/app
source venv/bin/activate

pkill gunicorn || true

python manage.py migrate
python manage.py collectstatic --noinput

gunicorn core.wsgi:application \
  --bind 127.0.0.1:8000 \
  --daemon
