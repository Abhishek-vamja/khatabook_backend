#!/bin/bash

TARGET="/home/ec2-user/khatabook_backend"

echo "Running clean step..."

if [ -d "$TARGET" ]; then
  echo "Cleaning $TARGET"
  rm -rf "$TARGET"/*
  rm -rf "$TARGET"/.[!.]* || true
  rm -rf "$TARGET"/..?* || true
else
  echo "Target directory does not exist, skipping clean"
fi

exit 0
