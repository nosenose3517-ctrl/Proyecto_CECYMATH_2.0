from django.shortcuts import render

def jerarquia_home(request):
    return render(request, 'jerarquia/index.html')
