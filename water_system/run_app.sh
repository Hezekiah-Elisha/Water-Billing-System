#!/usr/bin/env bash
source venv/bin/activate
export FLASK_APP=water_systemy.py
export FLASK_DEBUG=1
export FLASK_CONFIG=development
flask run --host='0.0.0.0' --port=7000
