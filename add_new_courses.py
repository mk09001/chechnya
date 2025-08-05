import os
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'physics_courses.settings')
django.setup()

from courses.models import Category, NobelLaureate, Course

def add_new_courses():
    # Получаем существующие категории и лауреатов
    quantum_category = Category.objects.get(name='Квантовая механика')
    relativity_category = Category.objects.get(name='Теория относительности')
    
    # Получаем существующих лауреатов
    feynman = NobelLaureate.objects.get(name='Ричард Фейнман')
    einstein = NobelLaureate.objects.get(name='Альберт Эйнштейн')
    
    # Курс 1: Теория относительности
    relativity_course = Course.objects.create(
        title='Теория относительности',
        slug='theory-of-relativity',
        description='Изучение специальной и общей теории относительности Эйнштейна',
        content="""Курс включает в себя:

• Специальная теория относительности
• Общая теория относительности
• Пространство-время и гравитация
• Эквивалентность массы и энергии
• Искривление пространства-времени
• Черные дыры и гравитационные волны

Материалы основаны на трудах Альберта Эйнштейна и современных исследованиях.""",
        price=15900.00,
        duration=48,
        level='intermediate',
        category=quantum_category,
        laureate=einstein
    )
    
    # Курс 2: Стандартная модель физики частиц
    standard_model_course = Course.objects.create(
        title='Стандартная модель физики частиц',
        slug='standard-model-particle-physics',
        description='Изучение фундаментальных частиц и их взаимодействий',
        content="""Курс включает в себя:

• Фундаментальные частицы (кварки, лептоны)
• Калибровочные бозоны
• Сильное взаимодействие (квантовая хромодинамика)
• Слабое взаимодействие
• Электромагнитное взаимодействие
• Бозон Хиггса и механизм Хиггса
• Эксперименты на Большом адронном коллайдере

Материалы основаны на современных исследованиях в ЦЕРН и других научных центрах.""",
        price=18900.00,
        duration=56,
        level='advanced',
        category=quantum_category,
        laureate=feynman
    )
    
    print(f"Добавлен курс: {relativity_course.title}")
    print(f"Добавлен курс: {standard_model_course.title}")
    
    return True

if __name__ == '__main__':
    if add_new_courses():
        print("Новые курсы успешно добавлены!")
    else:
        print("Ошибка при добавлении курсов") 