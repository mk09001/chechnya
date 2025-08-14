#!/usr/bin/env bash

# Простой скрипт сборки без виртуального окружения для Render.com
echo "🚀 Начинаем сборку проекта..."

# Установка зависимостей
echo "📦 Устанавливаем зависимости..."
pip install --upgrade pip
pip install -r requirements.txt

# Проверяем, что Django установлен
echo "✅ Проверяем установку Django..."
python -c "import django; print(f'Django version: {django.get_version()}')" || {
    echo "❌ Django не установлен, устанавливаем заново..."
    pip install Django==4.2.7
}

# Проверяем, что gunicorn установлен
echo "✅ Проверяем установку gunicorn..."
python -c "import gunicorn" || {
    echo "❌ gunicorn не установлен, устанавливаем..."
    pip install gunicorn==20.1.0
}

# Сборка статических файлов
echo "📁 Собираем статические файлы..."
python manage.py collectstatic --noinput --clear

# Миграции базы данных
echo "🗄️ Выполняем миграции..."
python manage.py migrate --noinput

echo "✅ Сборка завершена успешно!" 