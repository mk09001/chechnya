from django.urls import path
from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('laureates/', views.about_laureates, name='about_laureates'),
] 