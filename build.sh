#!/usr/bin/env bash

# Простой и надежный скрипт сборки для Render.com
echo "🚀 Начинаем сборку проекта..."

# Установка зависимостей
echo "📦 Устанавливаем зависимости..."
pip install --upgrade pip
pip install -r requirements.txt

# Сборка статических файлов
echo "📁 Собираем статические файлы..."
python manage.py collectstatic --noinput --clear

# Миграции базы данных
echo "🗄️ Выполняем миграции..."
python manage.py migrate --noinput

echo "✅ Сборка завершена успешно!" 