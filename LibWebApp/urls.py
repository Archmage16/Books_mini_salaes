from django.urls import path
from . import views

urlpatterns = [
    path( '',            views.home,         name='home' ),
    path( 'inp_author/', views.input_author, name='inp_author' ),
    path( 'inp_book/',   views.input_book,   name='inp_book' ),
    path('books/<int:book_id>', views.show_cover, name='show_cover'),
]