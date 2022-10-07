from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """
    Displays bag contents to user
    """
    return render(request, 'bag/bag.html')