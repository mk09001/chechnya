import os
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'physics_courses.settings')
django.setup()

from courses.models import Category, NobelLaureate, Course

def create_sample_data():
    # Создание категорий
    categories = [
        {
            'name': 'Квантовая механика',
            'slug': 'quantum-mechanics',
            'description': 'Изучение поведения материи и энергии на атомном и субатомном уровнях'
        },
        {
            'name': 'Теория относительности',
            'slug': 'relativity',
            'description': 'Физические теории о пространстве, времени и гравитации'
        },
        {
            'name': 'Ядерная физика',
            'slug': 'nuclear-physics',
            'description': 'Изучение ядер атомов и их взаимодействий'
        },
        {
            'name': 'Астрофизика',
            'slug': 'astrophysics',
            'description': 'Применение физических законов к изучению космических объектов'
        }
    ]
    
    for cat_data in categories:
        category, created = Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults=cat_data
        )
        if created:
            print(f"Создана категория: {category.name}")
    
    # Создание нобелевских лауреатов
    laureates = [
        {
            'name': 'Альберт Эйнштейн',
            'birth_year': 1879,
            'death_year': 1955,
            'country': 'Германия/США',
            'nobel_year': 1921,
            'discovery': 'За заслуги перед теоретической физикой и особенно за открытие закона фотоэлектрического эффекта',
            'biography': 'Альберт Эйнштейн - один из величайших физиков всех времен, создатель специальной и общей теории относительности.'
        },
        {
            'name': 'Нильс Бор',
            'birth_year': 1885,
            'death_year': 1962,
            'country': 'Дания',
            'nobel_year': 1922,
            'discovery': 'За заслуги в исследовании структуры атомов и испускаемого ими излучения',
            'biography': 'Нильс Бор - датский физик, один из основателей квантовой механики.'
        },
        {
            'name': 'Вернер Гейзенберг',
            'birth_year': 1901,
            'death_year': 1976,
            'country': 'Германия',
            'nobel_year': 1932,
            'discovery': 'За создание квантовой механики, применение которой привело к открытию аллотропных форм водорода',
            'biography': 'Вернер Гейзенберг - немецкий физик-теоретик, один из создателей квантовой механики.'
        },
        {
            'name': 'Ричард Фейнман',
            'birth_year': 1918,
            'death_year': 1988,
            'country': 'США',
            'nobel_year': 1965,
            'discovery': 'За фундаментальные работы по квантовой электродинамике',
            'biography': 'Ричард Фейнман - американский физик-теоретик, один из создателей квантовой электродинамики.'
        }
    ]
    
    for laureate_data in laureates:
        laureate, created = NobelLaureate.objects.get_or_create(
            name=laureate_data['name'],
            defaults=laureate_data
        )
        if created:
            print(f"Создан лауреат: {laureate.name}")
    
    # Создание курсов
    courses = [
        {
            'title': 'Основы квантовой механики',
            'slug': 'quantum-mechanics-basics',
            'category': Category.objects.get(slug='quantum-mechanics'),
            'laureate': NobelLaureate.objects.get(name='Нильс Бор'),
            'description': 'Введение в квантовую механику с изучением волновых функций и принципа неопределенности',
            'content': 'Курс включает изучение волновых функций, уравнения Шрёдингера, принципа неопределенности Гейзенберга и квантовых состояний.',
            'duration': 40,
            'level': 'beginner',
            'price': 15000.00
        },
        {
            'title': 'Теория относительности Эйнштейна',
            'slug': 'einstein-relativity',
            'category': Category.objects.get(slug='relativity'),
            'laureate': NobelLaureate.objects.get(name='Альберт Эйнштейн'),
            'description': 'Глубокое изучение специальной и общей теории относительности',
            'content': 'Курс охватывает специальную теорию относительности, общую теорию относительности, искривление пространства-времени и гравитационные волны.',
            'duration': 60,
            'level': 'intermediate',
            'price': 25000.00
        },
        {
            'title': 'Квантовая электродинамика',
            'slug': 'quantum-electrodynamics',
            'category': Category.objects.get(slug='quantum-mechanics'),
            'laureate': NobelLaureate.objects.get(name='Ричард Фейнман'),
            'description': 'Продвинутый курс по квантовой электродинамике с диаграммами Фейнмана',
            'content': 'Изучение квантовой электродинамики, диаграмм Фейнмана, перенормировки и взаимодействия света с веществом.',
            'duration': 80,
            'level': 'advanced',
            'price': 35000.00
        },
        {
            'title': 'Принцип неопределенности',
            'slug': 'uncertainty-principle',
            'category': Category.objects.get(slug='quantum-mechanics'),
            'laureate': NobelLaureate.objects.get(name='Вернер Гейзенберг'),
            'description': 'Детальное изучение принципа неопределенности Гейзенберга',
            'content': 'Глубокое изучение принципа неопределенности, его физического смысла и математического описания.',
            'duration': 30,
            'level': 'intermediate',
            'price': 18000.00
        }
    ]
    
    for course_data in courses:
        course, created = Course.objects.get_or_create(
            slug=course_data['slug'],
            defaults=course_data
        )
        if created:
            print(f"Создан курс: {course.title}")

if __name__ == '__main__':
    create_sample_data()
    print("Тестовые данные успешно созданы!") 