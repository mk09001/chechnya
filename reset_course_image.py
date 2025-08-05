import os
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'physics_courses.settings')
django.setup()

from courses.models import Course

def reset_course_image():
    try:
        course = Course.objects.get(slug='quantum-electrodynamics')
        print(f"Найден курс: {course.title}")
        
        # Убираем изображение
        course.image = ''
        course.save()
        
        # Возвращаем оригинальное содержание
        course.content = """Курс включает в себя:

• Изучение квантовой электродинамики (КЭД)
• Диаграммы Фейнмана и их интерпретация
• Перенормировка и устранение расходимостей
• Взаимодействие света с веществом
• Квантовая теория поля
• Применение КЭД в физике частиц

Материалы основаны на трудах Ричарда Фейнмана и других выдающихся физиков."""
        
        course.save()
        print("Изображение курса сброшено")
        return True
        
    except Course.DoesNotExist:
        print("Курс 'Квантовая электродинамика' не найден")
        return False

if __name__ == '__main__':
    if reset_course_image():
        print("Курс успешно обновлен!")
    else:
        print("Ошибка при обновлении курса") 