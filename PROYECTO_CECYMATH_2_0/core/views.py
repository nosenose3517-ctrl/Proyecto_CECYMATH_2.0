from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def suma(request):
    return render(request, "suma.html")

def resta(request):
    return render(request, "resta.html")

def multiplicacion(request):
    return render(request, "multiplicacion.html")

def polinomios(request):
    return render(request, "polinomios.html")

def recta(request):
    return render(request, "recta.html")

def jerarquia(request):
    return render(request, "jerarquia.html")

def factorizacion(request):
    return render(request, "factorizacion.html")

def ecuacion2(request):
    return render(request, "ecuacion2.html")

def ecuacion1(request):
    return render(request, "ecuacion1.html")
