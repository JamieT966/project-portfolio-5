from django.shortcuts import render

def profile(request):
    """
    Displays user's profile page
    """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)