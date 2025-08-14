# Physics Courses Platform

Платформа для изучения физики с курсами и информацией о лауреатах Нобелевской премии.

## 🚀 Features

- **Курсы по физике** - структурированные материалы для изучения
- **Лауреаты Нобелевской премии** - информация о выдающихся физиках
- **Корзина покупок** - система управления заказами
- **Адаптивный дизайн** - работает на всех устройствах

## 🛠️ Tech Stack

- **Backend**: Django 4.2.7
- **Database**: SQLite (development) / PostgreSQL (production)
- **Static Files**: WhiteNoise
- **Deployment**: Render.com

## 📋 Requirements

- Python 3.8+
- Django 4.2.7
- Pillow 10.0.1
- Gunicorn 21.2.0
- WhiteNoise 6.6.0

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

4. **Настройте переменные окружения**
   ```bash
   cp .env.example .env
   # Отредактируйте .env файл
   ```

5. **Выполните миграции**
   ```bash
   python manage.py migrate
   ```

6. **Создайте суперпользователя**
   ```bash
   python manage.py createsuperuser
   ```

7. **Запустите сервер**
   ```bash
   python manage.py runserver
   ```

8. **Откройте браузер**
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
4. **Укажите build command**: `./build.sh`
5. **Укажите start command**: `gunicorn physics_courses.wsgi:application`

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
├── build.sh                  # Build script for Render
└── README.md                 # This file
```

## 🔧 Configuration

### Environment Variables

- `SECRET_KEY` - Django secret key
- `DEBUG` - Debug mode (True/False)
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts
- `DATABASE_URL` - Database connection string

### Database

- **Development**: SQLite3
- **Production**: PostgreSQL (recommended)

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

If you have any questions or need help, please open an issue on GitHub.

---

**Happy coding! 🎉** 