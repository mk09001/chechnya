# 🚀 Быстрый старт для деплоя

## 📋 Что уже готово:
✅ Все необходимые файлы созданы  
✅ Настройки для production настроены  
✅ Конфигурация Render подготовлена  

## 🎯 Следующие шаги:

### 1. Закоммитьте и запушьте код в GitHub
```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

### 2. Перейдите на [render.com](https://render.com)
- Создайте аккаунт
- Подключите GitHub репозиторий

### 3. Создайте Web Service
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn physics_courses.wsgi_production:application`

### 4. Создайте PostgreSQL базу данных
- Название: `physics-courses-db`
- База: `physics_courses`

### 5. Добавьте переменные окружения
Скопируйте из файла `render_env_vars.txt`

## 📖 Подробные инструкции:
- `DEPLOYMENT_INSTRUCTIONS.md` - пошаговый гайд
- `DEPLOYMENT_CHECKLIST.md` - чек-лист готовности

## 🔧 Если что-то не работает:
1. Проверьте логи в Render
2. Убедитесь, что все переменные настроены
3. Проверьте, что база данных доступна

---

**Удачи! 🎉**
