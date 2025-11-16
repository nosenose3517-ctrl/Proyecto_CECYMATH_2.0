from django.shortcuts import render

def segundo_home(request):
    return render(request, 'segundo/index.html')
