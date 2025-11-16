from django.urls import path
from . import views

urlpatterns = [
    path('', views.resta_home, name='resta_home'),
]
