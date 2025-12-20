#!/bin/bash
set -e

TARGET="/home/ec2-user/khatabook_backend"

echo "Cleaning old code..."

if [ -d "$TARGET" ]; then
  rm -rf "$TARGET"
fi

mkdir -p "$TARGET"
chown -R ec2-user:ec2-user "$TARGET"

echo "Cleanup completed."
