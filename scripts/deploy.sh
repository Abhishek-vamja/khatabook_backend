#!/bin/bash
set -e
set -x

APP_DIR=/home/ec2-user/khatabook_backend

cd $APP_DIR
source venv/bin/activate

pkill -f gunicorn || true

venv/bin/gunicorn khatabook_backend.wsgi:application \
  --bind 0.0.0.0:8000 \
  --daemon
