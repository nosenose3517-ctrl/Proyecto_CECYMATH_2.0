from django.shortcuts import render

def recta_home(request):
    return render(request, 'recta/index.html')
