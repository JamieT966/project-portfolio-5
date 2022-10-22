from django.shortcuts import render
from .models import NewsletterSubscriber
from .forms import NewsletterSubscriberForm
from django.contrib import messages


def display_newsletter_fom(request):
    form = NewsletterSubscriberForm(request.POST or None)

    if form.is_valid():
        email = form.cleaned_data['email']
        instance = form.save(commit=False)

        if NewsletterSubscriber.objects.filter(email=instance.email).exists():
            messages.error(request, 'Sorry, this email already exists in our system.')
        else:
            instance.save()

        context = {
            'form': form,
        }

        template = 'index.html'

        return render(request, template, context)