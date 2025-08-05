from django.shortcuts import render
from courses.models import Course, NobelLaureate, Category

def landing_page(request):
    """Главная страница лендинга"""
    featured_courses = Course.objects.filter(is_active=True)[:6]
    laureates = NobelLaureate.objects.all()[:4]
    categories = Category.objects.all()
    
    context = {
        'featured_courses': featured_courses,
        'laureates': laureates,
        'categories': categories,
    }
    return render(request, 'landing/landing.html', context)

def about_laureates(request):
    """Страница о нобелевских лауреатах"""
    laureates = NobelLaureate.objects.all().order_by('nobel_year')
    
    context = {
        'laureates': laureates,
    }
    return render(request, 'landing/about_laureates.html', context)
