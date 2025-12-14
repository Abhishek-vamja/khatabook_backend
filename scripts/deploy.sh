#!/bin/bash

echo "=== DEPLOY STARTED ==="

cd /home/ec2-user/khatabook_backend || exit 1

echo "Activate virtualenv"
source venv/bin/activate

echo "Stop gunicorn"
pkill gunicorn || true

echo "Install dependencies"
pip install -r requirements.txt

echo "Run migrations"
python manage.py migrate || true

echo "Collect static"
python manage.py collectstatic --noinput || true

echo "Start gunicorn"
gunicorn khatabook_backend.wsgi:application \
  --bind 127.0.0.1:8000 \
  --daemon

echo "=== DEPLOY FINISHED SUCCESSFULLY ==="
exit 0
