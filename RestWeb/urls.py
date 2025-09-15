from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
route = DefaultRouter()

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(route.urls)),
    path('api/Employers/', EmployerView, name='employers'),
    path('api/Employe/<int:id>/', OneEmployerView, name='employe'),
]
