from django.contrib import admin
from .models import NobelLaureate, Category, Course, Review

@admin.register(NobelLaureate)
class NobelLaureateAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'nobel_year', 'discovery']
    list_filter = ['country', 'nobel_year']
    search_fields = ['name', 'discovery']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'laureate', 'price', 'level', 'is_active']
    list_filter = ['category', 'level', 'is_active', 'created_at']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['price', 'is_active']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['course', 'name', 'rating', 'is_approved', 'created_at']
    list_filter = ['rating', 'is_approved', 'created_at']
    search_fields = ['name', 'comment']
    list_editable = ['is_approved']
    readonly_fields = ['created_at']
