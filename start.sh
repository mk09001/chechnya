#!/usr/bin/env bash

# Скрипт запуска приложения
echo "🚀 Запускаем приложение..."

# Проверяем наличие gunicorn
if command -v gunicorn &> /dev/null; then
    echo "✅ gunicorn найден, запускаем..."
    gunicorn physics_courses.wsgi_production:application
elif python -c "import gunicorn" &> /dev/null; then
    echo "✅ gunicorn найден через python -m, запускаем..."
    python -m gunicorn physics_courses.wsgi_production:application
else
    echo "❌ gunicorn не найден, устанавливаем..."
    pip install gunicorn==20.1.0
    gunicorn physics_courses.wsgi_production:application
fi 