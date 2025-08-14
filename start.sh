#!/usr/bin/env bash

# Скрипт запуска приложения
echo "🚀 Запускаем приложение..."

# Активируем виртуальное окружение (если есть)
if [ -d ".venv" ]; then
    echo "🔧 Активируем виртуальное окружение..."
    source .venv/bin/activate
fi

# Проверяем, что Django установлен
echo "✅ Проверяем Django..."
python -c "import django; print(f'Django version: {django.get_version()}')" || {
    echo "❌ Django не найден, устанавливаем..."
    pip install Django==4.2.7
}

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