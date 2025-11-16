from django.shortcuts import render

def suma_home(request):
    return render(request, 'suma/index.html')

