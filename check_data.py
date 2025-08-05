import os
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'physics_courses.settings')
django.setup()

from courses.models import Category, NobelLaureate

print("=== КАТЕГОРИИ ===")
for category in Category.objects.all():
    print(f"- {category.name}")

print("\n=== ЛАУРЕАТЫ ===")
for laureate in NobelLaureate.objects.all():
    print(f"- {laureate.name}") 