from django.contrib import admin
from django.urls import path
from Show_names import views

urlpatterns = [
    path('', views.index, name='index'),
    path('character/<int:char_id>/', views.character_detail, name='character_detail'),

    path('add-character/', views.add_character, name='add_character'),
]
