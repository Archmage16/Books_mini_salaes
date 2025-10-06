from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),

    path('history', views.history_info, name='history'),
    path('history/1885', views.info_1885, name='eight'),
    path('history/1914', views.info_1914, name='nine'),
    
    path('cities', views.cities_info, name='cities'),
    path('cities/Paris', views.Paris_info, name='cities_Paris'),
    path('cities/Marseille', views.Marseille_info, name='cities_Marseille'),

    path('cities/Paris/1924', views.Paris_1924, name='paris_1924'),
    path('cities/Marseille/1956', views.Marseille_1956, name='marseille_1956'),

    
    path('facts', views.facts_info, name='facts'),

]