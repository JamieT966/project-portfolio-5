from django.shortcuts import render


def index(request):
    """
    Displays homepage
    """
    return render(request, 'home/index.html')
