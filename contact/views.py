from django.shortcuts import render
from django.contrib import messages
from .forms import DisplayContactForm
from django.core.mail import send_mail


def contact(request):
    """
    Displays contact form
    When contact form is submitted send user success message
    Sends email to staff about message
    """
    form = DisplayContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        product = form.cleaned_data['product']

        form = DisplayContactForm()
        messages.success(
            request,
            'Message received,'
            'a member of our team will get back to you shortly.')

        # Send an email to Chemstore Admin
        send_mail(
            f'New Message from {name} relating to {product}',
            message,
            email,
            ['jamie@chem-eshop.ie']
            )

    template = 'contact/contact.html'
    context = {
        'form': form
    }

    return render(request, template, context)
