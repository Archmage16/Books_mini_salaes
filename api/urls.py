from django.urls import path
from .views import *

urlpatterns = [
    path('message/', MessageView.as_view(), name='message'),
    path('messages/', Print_mess, name='print_messages'),
    path('register/', RegisterUser.as_view()),
    path('users/', Print_user, name='print_users'),
]