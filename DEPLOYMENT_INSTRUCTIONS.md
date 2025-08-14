# 🚀 Инструкции по деплою на Render.com

## 📋 Подготовка проекта

### 1. Убедитесь, что все файлы готовы:
- ✅ `requirements.txt` - зависимости Python
- ✅ `build.sh` - скрипт сборки
- ✅ `render.yaml` - конфигурация Render
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
SECRET_KEY=django-insecure-#9fen+d-ird))#92**w2bwzvj#4k+)*si^-0a2*zm06f_wpn$3
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
```

**Примечание**: `DATABASE_URL` будет автоматически добавлен при создании базы данных.

### Шаг 6: Создание базы данных
1. Нажмите "New +" → "PostgreSQL"
2. **Name**: `physics-courses-db`
3. **Database**: `physics_courses`
4. **User**: `physics_courses_user`
5. **Region**: тот же, что и у веб-сервиса

### Шаг 7: Запуск деплоя
1. Нажмите "Create Web Service"
2. Render автоматически:
   - Установит зависимости
   - Выполнит `build.sh`
   - Запустит сервер
   - Создаст URL для вашего приложения

## 🔧 Возможные проблемы и решения

### Ошибка: "Module not found"
- Убедитесь, что все зависимости в `requirements.txt`
- Проверьте, что `build.sh` выполняется без ошибок

### Ошибка: "Database connection failed"
- Проверьте, что база данных создана
- Убедитесь, что `DATABASE_URL` правильно настроен

### Ошибка: "Static files not found"
- Проверьте, что `build.sh` содержит `python manage.py collectstatic`
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
