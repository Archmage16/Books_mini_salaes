from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('time/', views.get_time),
    path('date/', views.get_date),
]
