from django.shortcuts import render

def primer_home(request):
    return render(request, 'primer/index.html')
