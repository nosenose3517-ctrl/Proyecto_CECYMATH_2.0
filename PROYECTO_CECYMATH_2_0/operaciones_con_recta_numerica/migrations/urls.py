from django.urls import path
from . import views

urlpatterns = [
    path('', views.recta_home, name='recta_home'),
]
