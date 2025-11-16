from django.shortcuts import render

def factorizacion_home(request):
    return render(request, 'factorizacion/index.html')
