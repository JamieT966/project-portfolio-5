from django.shortcuts import render

# Create your views here.

def index(request):
    """
    Displays homepage
    """
    return render(request, 'home/index.html')