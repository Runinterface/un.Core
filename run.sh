#!/bin/bash

FLASK_APP=src/uncore.py FLASK_ENV=$1 flask run --port 5000