from django.shortcuts import render

def multiplicacion_home(request):
    return render(request, 'multiplicacion/index.html')
