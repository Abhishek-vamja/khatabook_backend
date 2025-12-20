#!/bin/bash
#!/bin/bash
set -x
set -e

APP_DIR=/home/ec2-user/khatabook_backend

echo "Starting install..."

# Ensure correct ownership
sudo chown -R ec2-user:ec2-user /home/ec2-user

# Go to app directory
cd $APP_DIR

# Create venv if not exists
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

echo "Install completed successfully"

cd /home/ec2-user/khatabook_backend

source venv/bin/activate

pkill gunicorn || true

python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn khatabook_backend.wsgi:application \
  --bind 127.0.0.1:8000 \
  --workers 3 \
  --daemon
