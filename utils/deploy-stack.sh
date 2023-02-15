#!/usr/bin/sh
#!/bin/bash
# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
BASE_DIR=$(dirname "$SCRIPT")

 cd "$BASE_DIR/../"
 docker compose build
 docker compose up -d
