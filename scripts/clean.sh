#!/bin/bash
set -e

APP_DIR=/home/ec2-user/khatabook_backend

echo "Cleaning old deployment..."
rm -rf $APP_DIR/*
