#!/bin/bash
cd /home/ec2-user/khatabook_backend
source venv/bin/activate

pkill gunicorn || true

python manage.py migrate
python manage.py collectstatic --noinput

gunicorn khatabook_backend.wsgi:application   --bind 127.0.0.1:8000   --daemon