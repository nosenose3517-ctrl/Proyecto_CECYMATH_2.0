from django.urls import path
from . import views

urlpatterns = [
    path('', views.multiplicacion_home, name='multiplicacion_home'),
]
