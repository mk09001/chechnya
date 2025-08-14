# 🚀 Инструкции по деплою на Render.com

## 📋 Подготовка проекта

### 1. Убедитесь, что все файлы готовы:
- ✅ `requirements.txt` - зависимости Python
- ✅ `build.sh` - скрипт сборки
- ✅ `physics_courses/production_settings.py` - production настройки
- ✅ `physics_courses/wsgi_production.py` - production WSGI

### 2. Проверьте .gitignore:
- ✅ Исключены `db.sqlite3`, `media/`, `staticfiles/`
- ✅ Исключены `.env` файлы
- ✅ Исключены `__pycache__/` и другие временные файлы

## 🌐 Деплой на Render.com

### Шаг 1: Создание аккаунта
1. Зайдите на [render.com](https://render.com)
2. Создайте аккаунт или войдите через GitHub

### Шаг 2: Подключение репозитория
1. Нажмите "New +" → "Web Service"
2. Подключите ваш GitHub репозиторий
3. Выберите ветку (обычно `main` или `master`)

### Шаг 3: Настройка сервиса
1. **Name**: `physics-courses` (или любое другое)
2. **Environment**: `Python 3`
3. **Region**: выберите ближайший к вашим пользователям
4. **Branch**: `main` (или ваша основная ветка)
5. **Root Directory**: оставьте пустым (если проект в корне)

### Шаг 4: Команды
1. **Build Command**: `./build.sh`
2. **Start Command**: `gunicorn physics_courses.wsgi_production:application`

### Шаг 5: Переменные окружения
Добавьте следующие переменные в разделе "Environment Variables":

```
SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com,localhost,127.0.0.1,.onrender.com,.render.com
```

**Важно**: Замените `your-app-name.onrender.com` на реальный URL вашего приложения на Render.

### Шаг 6: Запуск деплоя
1. Нажмите "Create Web Service"
2. Render автоматически:
   - Выполнит `./build.sh` (установка зависимостей, collectstatic, migrate)
   - Запустит `gunicorn physics_courses.wsgi_production:application`
   - Создаст URL для вашего приложения

## 🔧 Возможные проблемы и решения

### Ошибка: "Bad Request (400)"
- **Причина**: Неправильные настройки ALLOWED_HOSTS
- **Решение**: Убедитесь, что в переменных окружения указан правильный домен:
  ```
  ALLOWED_HOSTS=your-app-name.onrender.com,localhost,127.0.0.1,.onrender.com,.render.com
  ```

### Ошибка: "Module not found"
- Убедитесь, что все зависимости в `requirements.txt`
- Проверьте, что нет лишних зависимостей

### Ошибка: "Database connection failed"
- SQLite файл будет создан автоматически
- Убедитесь, что у приложения есть права на запись в директорию

### Ошибка: "Static files not found"
- `build.sh` автоматически выполнит `collectstatic`
- Убедитесь, что `STATIC_ROOT` настроен в `production_settings.py`

### Ошибка: "Permission denied" в build.sh
- Убедитесь, что `build.sh` имеет права на выполнение
- В Render это обычно не проблема

## 📱 Проверка работы

После успешного деплоя:
1. Откройте URL вашего приложения
2. Проверьте главную страницу
3. Проверьте страницу курсов
4. Проверьте страницу лауреатов
5. Проверьте админ-панель Django

## 🔄 Обновление приложения

При каждом push в GitHub:
1. Render автоматически обнаружит изменения
2. Запустит новый деплой
3. Обновит ваше приложение

## 📊 Мониторинг

В Render вы можете:
- Видеть логи приложения
- Мониторить использование ресурсов
- Настраивать алерты
- Управлять переменными окружения

## 🆘 Поддержка

Если что-то не работает:
1. Проверьте логи в Render
2. Убедитесь, что все переменные окружения настроены
3. Проверьте, что база данных доступна
4. Обратитесь к документации Render или создайте тикет

---

**Удачи с деплоем! 🎉** 