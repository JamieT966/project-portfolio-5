from django.shortcuts import render
from django.contrib import messages
from .models import ContactForm
from .forms import DisplayContactForm


def contact(request):
    """
    Displays contact form
    """
    form = DisplayContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = DisplayContactForm()
        messages.success(request, 'Message received, a member of our team will get back to you shortly.')

    template = 'contact/contact.html'
    context = {
        'form': form
    }

    return render(request, template, context)
