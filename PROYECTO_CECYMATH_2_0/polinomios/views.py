from django.shortcuts import render

def polinomios_home(request):
    return render(request, 'polinomios/index.html')
