from django.shortcuts import render

def resta_home(request):
    return render(request, 'resta/index.html')
