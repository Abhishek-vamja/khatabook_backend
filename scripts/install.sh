#!/bin/bash
cd /home/ec2-user/khatabook_backend
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
