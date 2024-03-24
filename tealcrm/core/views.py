from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')



def about(request):
    return render(request, 'core/about.html')


def clients(request):
    return render(request, 'core/clients.html')

def estate(request):
    return render(request, 'core/estate.html')