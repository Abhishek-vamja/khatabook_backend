#!/bin/bash

TARGET="/home/ec2-user/khatabook_backend"

echo "Cleaning old code..."

if [ -d "$TARGET" ]; then
  rm -rf "$TARGET"/*
  rm -rf "$TARGET"/.[!.]* || true
  rm -rf "$TARGET"/..?* || true
fi

exit 0
