from django.urls import path
from . import views

urlpatterns = [
    path('', views.segundo_home, name='segundo_home'),
]
