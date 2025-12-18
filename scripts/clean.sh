#!/bin/bash
set -e

TARGET="/home/ec2-user/khatabook_backend"

echo "Cleaning old deployment..."
rm -rf $TARGET/*
rm -rf $TARGET/.[!.]*
rm -rf $TARGET/..?*
