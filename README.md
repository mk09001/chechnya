# 🚀 Физика Плюс - Интернет-магазин курсов теоретической физики

Интернет-магазин курсов по теоретической физике, связанных с открытиями нобелевских лауреатов.

## 🎯 Описание проекта

Проект представляет собой веб-приложение для продажи онлайн-курсов по теоретической физике. Каждый курс связан с конкретным открытием нобелевского лауреата и включает в себя:

- **Курсы по физике** - структурированные образовательные программы
- **Нобелевские лауреаты** - информация о ученых и их открытиях
- **Корзина покупок** - функционал для оформления заказов
- **Система отзывов** - оценка и комментарии пользователей

## 🛠 Технологии

- **Framework**: Django 4.2.7
- **Language**: Python 3.8+
- **Database**: SQLite (development) / PostgreSQL (production)
- **Static Files**: WhiteNoise
- **Deployment**: Render.com

## 📋 Requirements

- Python 3.8+
- Django 4.2.7
- Gunicorn 20.1.0
- WhiteNoise 6.5.0
- psycopg2-binary 2.9.6
- dj-database-url 2.0.0

## 🚀 Quick Start

### Local Development

1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/your-username/physics-courses.git
   cd physics-courses
   ```

2. **Создайте виртуальное окружение**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Установите зависимости**
   ```bash
   pip install -r requirements.txt
   ```

4. **Выполните миграции**
   ```bash
   python manage.py migrate
   ```

5. **Создайте суперпользователя**
   ```bash
   python manage.py createsuperuser
   ```

6. **Запустите сервер**
   ```bash
   python manage.py runserver
   ```

7. **Откройте браузер**
   ```
   http://127.0.0.1:8000/
   ```

### Production Deployment

1. **Настройте переменные окружения**
   - `SECRET_KEY` - секретный ключ Django
   - `DEBUG` - False для production
   - `ALLOWED_HOSTS` - разрешенные домены
   - `DATABASE_URL` - URL базы данных PostgreSQL

2. **Соберите статические файлы**
   ```bash
   python manage.py collectstatic
   ```

3. **Выполните миграции**
   ```bash
   python manage.py migrate
   ```

## 🌐 Deployment on Render.com

1. **Подключите GitHub репозиторий**
2. **Создайте Web Service**
3. **Настройте переменные окружения**
4. **Build Command**: оставьте пустым (используется Procfile)
5. **Start Command**: оставьте пустым (используется Procfile)

## 📁 Project Structure

```
physics_courses/
├── physics_courses/          # Main project settings
├── landing/                  # Landing page app
├── courses/                  # Courses management app
├── cart/                     # Shopping cart app
├── templates/                # HTML templates
├── static/                   # Static files (CSS, JS, images)
├── media/                    # User uploaded files
├── requirements.txt          # Python dependencies
├── Procfile                  # Procfile for Render deployment
└── README.md                 # This file
```

## 🎨 Features

### Основной функционал:
- **Главная страница** - информация о проекте и курсах
- **Каталог курсов** - список всех доступных курсов
- **Детальная страница курса** - полная информация о курсе
- **Страница лауреатов** - информация о нобелевских лауреатах
- **Корзина покупок** - добавление и оформление заказов
- **Админ-панель** - управление контентом

### Технические особенности:
- **Адаптивный дизайн** - работает на всех устройствах
- **SEO-оптимизация** - правильная структура URL и мета-теги
- **Безопасность** - защита от CSRF, XSS и других атак
- **Производительность** - оптимизация статических файлов

## 🔧 Configuration

### Переменные окружения:
- `SECRET_KEY` - секретный ключ Django
- `DEBUG` - режим отладки (True/False)
- `ALLOWED_HOSTS` - список разрешенных доменов
- `DATABASE_URL` - URL базы данных

### Настройки базы данных:
- **Development**: SQLite (по умолчанию)
- **Production**: PostgreSQL (через DATABASE_URL)

## 📱 API Endpoints

Основные URL проекта:
- `/` - главная страница
- `/courses/` - список курсов
- `/courses/<slug>/` - детальная страница курса
- `/laureates/` - список лауреатов
- `/cart/` - корзина покупок
- `/admin/` - админ-панель

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)

## 🙏 Acknowledgments

- Django framework
- Render.com for hosting
- All contributors and supporters

---

**Удачи с изучением физики! 🚀** 