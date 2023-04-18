#!/bin/bash -x

./.venv/bin/python3 manage.py  migrate --noinput || exit 1
exec "$@"
