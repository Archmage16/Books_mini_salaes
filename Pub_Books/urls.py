from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("authors/", views.author_list, name="author_list"),
    path("authors/add/", views.author_create, name="author_add"),

    path("publishers/", views.publisher_list, name="publisher_list"),
    path("publishers/add/", views.publisher_create, name="publisher_add"),

    path("books/", views.book_list, name="book_list"),
    path("books/add/", views.book_create, name="book_add"),

    path("publications/", views.publication_list, name="publication_list"),
    path("publications/add/", views.publication_create, name="publication_add"),

    path("sales/", views.sales_list, name="sales_list"),
    path("sales/add/", views.sales_create, name="sales_add"),
]
