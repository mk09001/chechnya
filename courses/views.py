from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Course, Category, Review
from .forms import ReviewForm

# Create your views here.

def course_list(request):
    """Список всех курсов"""
    category_slug = request.GET.get('category')
    level = request.GET.get('level')
    
    courses = Course.objects.filter(is_active=True)
    
    if category_slug:
        courses = courses.filter(category__slug=category_slug)
    
    if level:
        courses = courses.filter(level=level)
    
    # Пагинация
    paginator = Paginator(courses, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'current_category': category_slug,
        'current_level': level,
    }
    return render(request, 'courses/course_list.html', context)

def course_detail(request, slug):
    """Детальная страница курса"""
    course = get_object_or_404(Course, slug=slug, is_active=True)
    reviews = Review.objects.filter(course=course, is_approved=True)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.course = course
            review.save()
            form = ReviewForm()  # Очищаем форму
    else:
        form = ReviewForm()
    
    context = {
        'course': course,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'courses/course_detail.html', context)
