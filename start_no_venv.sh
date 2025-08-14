#!/usr/bin/env bash

# Простой скрипт запуска без виртуального окружения
echo "🚀 Запускаем приложение..."

# Проверяем Django
python -c "import django" || pip install Django==4.2.7

# Запускаем gunicorn
python -m gunicorn physics_courses.wsgi_production:application 