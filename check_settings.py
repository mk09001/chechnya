#!/usr/bin/env python
"""
Скрипт для проверки настроек Django в production окружении
"""
import os
import sys
import django

# Добавляем путь к проекту
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Устанавливаем переменные окружения для тестирования
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'physics_courses.production_settings')

# Инициализируем Django
django.setup()

from django.conf import settings

print("🔍 Проверка настроек Django:")
print("=" * 50)

print(f"DEBUG: {settings.DEBUG}")
print(f"ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
print(f"SECRET_KEY: {'*' * 20 if settings.SECRET_KEY else 'НЕ УСТАНОВЛЕН'}")
print(f"DATABASES: {list(settings.DATABASES.keys())}")

# Проверяем базу данных
db_config = settings.DATABASES['default']
print(f"Database Engine: {db_config['ENGINE']}")
print(f"Database Name: {db_config['NAME']}")

# Проверяем статические файлы
print(f"STATIC_URL: {settings.STATIC_URL}")
print(f"STATIC_ROOT: {settings.STATIC_ROOT}")
print(f"STATICFILES_DIRS: {settings.STATICFILES_DIRS}")

# Проверяем приложения
print(f"INSTALLED_APPS: {len(settings.INSTALLED_APPS)} приложений")

print("=" * 50)
print("✅ Проверка завершена!") 