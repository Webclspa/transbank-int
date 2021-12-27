from django.urls import path
from core import views

urlpatterns = [
    path('', views.base, name='base'),
    path('exito', views.success, name='success')
]

