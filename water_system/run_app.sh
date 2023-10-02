#!/usr/bin/env bash
export FLASK_APP=water_systemy.py
export FLASK_DEBUG=1
export FLASK_CONFIG=development
# export FLASK_ENV=development
flask db init
flask run --host='0.0.0.0' --port=7000