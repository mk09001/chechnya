from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class NobelLaureate(models.Model):
    """Модель для нобелевских лауреатов по физике"""
    name = models.CharField(max_length=200, verbose_name="Имя")
    birth_year = models.IntegerField(verbose_name="Год рождения")
    death_year = models.IntegerField(null=True, blank=True, verbose_name="Год смерти")
    country = models.CharField(max_length=100, verbose_name="Страна")
    nobel_year = models.IntegerField(verbose_name="Год получения Нобелевской премии")
    discovery = models.TextField(verbose_name="Открытие/достижение")
    photo = models.FileField(upload_to='laureates/', verbose_name="Фотография")
    biography = models.TextField(verbose_name="Биография")
    
    class Meta:
        verbose_name = "Нобелевский лауреат"
        verbose_name_plural = "Нобелевские лауреаты"
        ordering = ['nobel_year']
    
    def __str__(self):
        return f"{self.name} ({self.nobel_year})"

class Category(models.Model):
    """Категории курсов"""
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="URL")
    description = models.TextField(verbose_name="Описание")
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return self.name

class Course(models.Model):
    """Модель для курсов теоретической физики"""
    title = models.CharField(max_length=200, verbose_name="Название курса")
    slug = models.SlugField(unique=True, verbose_name="URL")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    laureate = models.ForeignKey(NobelLaureate, on_delete=models.CASCADE, verbose_name="Нобелевский лауреат")
    description = models.TextField(verbose_name="Описание")
    content = models.TextField(verbose_name="Содержание курса")
    duration = models.IntegerField(verbose_name="Длительность (часы)")
    level = models.CharField(max_length=50, choices=[
        ('beginner', 'Начинающий'),
        ('intermediate', 'Средний'),
        ('advanced', 'Продвинутый'),
    ], verbose_name="Уровень сложности")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.FileField(upload_to='courses/', verbose_name="Изображение курса")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class Review(models.Model):
    """Отзывы о курсах"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews', verbose_name="Курс")
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="Оценка")
    comment = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_approved = models.BooleanField(default=False, verbose_name="Одобрен")
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Отзыв от {self.name} на {self.course.title}"
