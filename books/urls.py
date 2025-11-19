from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_books, name='search'),
    path('books/', views.book_list, name='book_list'),
]
