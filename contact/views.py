from django.shortcuts import render
from .models import ContactForm


def contact(request):
    """
    Displays contact form
    """
    return render(request, 'contact/contact.html')
