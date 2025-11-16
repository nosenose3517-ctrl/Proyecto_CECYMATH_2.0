from django.urls import path
from . import views

urlpatterns = [
    path('', views.factorizacion_home, name='factorizacion_home'),
]
