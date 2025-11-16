from django.urls import path
from . import views

urlpatterns = [
    path('', views.jerarquia_home, name='jerarquia_home'),
]
