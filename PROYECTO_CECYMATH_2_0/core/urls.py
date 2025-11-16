from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('suma/', views.suma, name='suma'),
    path('resta/', views.resta, name='resta'),
    path('multiplicacion/', views.multiplicacion, name='multiplicacion'),
    path('polinomios/', views.polinomios, name='polinomios'),
    path('operaciones_con_recta_numerica/', views.recta, name='recta'),
    path('jerarquia_de_operaciones/', views.jerarquia, name='jerarquia'),
    path('factorizacion/', views.factorizacion, name='factorizacion'),
    path('ecuaciones_de_segundo_grado_con_formula_general/', views.ecuacion2, name='ecuacion2'),
    path('ecuaciones_de_primer_grado/', views.ecuacion1, name='ecuacion1'),
]
