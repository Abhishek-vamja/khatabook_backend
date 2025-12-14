#!/bin/bash
set -e

exec > /tmp/ec2-pipeline-deploy.log 2>&1

cd /home/ec2-user/khatabook_backend

source venv/bin/activate

pkill gunicorn || true

pip install -r requirements.txt
python manage.py migrate || true
python manage.py collectstatic --noinput || true

gunicorn khatabook_backend.wsgi:application \
  --bind 127.0.0.1:8000 \
  --daemon

exit 0
