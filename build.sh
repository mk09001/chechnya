#!/usr/bin/env bash

# Простой скрипт сборки для Render.com
echo "🚀 Начинаем сборку проекта..."

# Установка зависимостей
echo "📦 Устанавливаем зависимости..."
pip install -r requirements.txt

# Сборка статических файлов
echo "📁 Собираем статические файлы..."
python manage.py collectstatic --noinput

# Миграции базы данных
echo "🗄️ Выполняем миграции..."
python manage.py migrate

echo "✅ Сборка завершена успешно!" 