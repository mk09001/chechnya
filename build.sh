#!/usr/bin/env bash

# Простой и надежный скрипт сборки для Render.com
echo "🚀 Начинаем сборку проекта..."

# Установка зависимостей
echo "📦 Устанавливаем зависимости..."
pip install --upgrade pip
pip install -r requirements.txt

# Дополнительная установка gunicorn для гарантии
echo "🔧 Устанавливаем gunicorn..."
pip install gunicorn==20.1.0

# Проверяем, что gunicorn установлен
echo "✅ Проверяем установку gunicorn..."
which gunicorn || echo "❌ gunicorn не найден в PATH"
gunicorn --version || echo "❌ gunicorn не работает"

# Сборка статических файлов
echo "📁 Собираем статические файлы..."
python manage.py collectstatic --noinput --clear

# Миграции базы данных
echo "🗄️ Выполняем миграции..."
python manage.py migrate --noinput

echo "✅ Сборка завершена успешно!" 