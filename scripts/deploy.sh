#!/bin/bash
set -e

cd /home/ec2-user/khatabook_backend
source venv/bin/activate

python manage.py migrate --noinput
python manage.py collectstatic --noinput

systemctl restart gunicorn