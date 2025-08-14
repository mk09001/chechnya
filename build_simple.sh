#!/usr/bin/env bash

# Максимально простой скрипт сборки
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate 