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
            form = NewsletterSubscriberForm()
            messages.success(request, 'Thanks for signing up to the Hazmat Bulletin!')

    context = {
        'form': form,
    }

    template = 'newsletter/sign_up.html'

    return render(request, template, context)


def unsubcribe_newsletter(request):
    form = NewsletterSubscriberForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterSubscriber.objects.filter(email=instance.email).exists():
            NewsletterSubscriber.objects.filter(email=instance.email).delete()
            form = NewsletterSubscriberForm()
            messages.success(request, 'Your email address has been removed from our system. We are sorry to see you go :(')

        else:
            messages.error(request, 'We are unable to find that email address in our system.')

    context = {
        'form': form,
    }

    template = 'newsletter/unsubscribe.html'

    return render(request, template, context)