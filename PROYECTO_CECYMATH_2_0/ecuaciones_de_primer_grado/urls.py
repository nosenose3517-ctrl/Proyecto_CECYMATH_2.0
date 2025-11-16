from django.urls import path
from . import views

urlpatterns = [
    path('', views.primer_home, name='primer_home'),
]
