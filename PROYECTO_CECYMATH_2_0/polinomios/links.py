from django.urls import path
from . import views

urlpatterns = [
    path('', views.polinomios_home, name='polinomios_home'),
]
