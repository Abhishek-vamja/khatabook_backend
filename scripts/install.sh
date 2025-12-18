#!/bin/bash
set -e

cd /home/ec2-user/khatabook_backend

python3 -m venv venv || true
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
