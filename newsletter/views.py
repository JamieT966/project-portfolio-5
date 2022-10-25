from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.http import HttpResponse
from .models import NewsletterSubscriber
from .forms import NewsletterSubscriberForm
from .admin import NewsletterExport


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
            # Sends email to newsletter subscriber
            subject = 'Thanks for signing up to the Hazmat Bulletin'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [instance.email]
            with open(str(settings.BASE_DIR) + '/newsletter/templates/newsletter/emails/sign_up_email.txt') as i:
                body = i.read()
            message = EmailMultiAlternatives(subject=subject, body=body, from_email=from_email, to=to_email)
            html_email = get_template('newsletter/emails/sign_up_email.html').render()
            message.attach_alternative(html_email, 'text/html')
            message.send()

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
            subject = 'You have unsubscribed from the Hazmat Bulletin'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [instance.email]
            with open(str(settings.BASE_DIR) + '/newsletter/templates/newsletter/emails/unsubscribe_email.txt') as i:
                body = i.read()
            message = EmailMultiAlternatives(subject=subject, body=body, from_email=from_email, to=to_email)
            html_email = get_template('newsletter/emails/unsubscribe_email.html').render()
            message.attach_alternative(html_email, 'text/html')
            message.send()

        else:
            messages.error(request, 'We are unable to find that email address in our system.')

    context = {
        'form': form,
    }

    template = 'newsletter/unsubscribe.html'

    return render(request, template, context)


def export_newsletter(request, format):
    newsletter_export = NewsletterExport()
    dataset = newsletter_export.export()
    if format == 'csv':
        dataset_format = dataset.csv

    response = HttpResponse(dataset_format, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=newsletter.csv'
    return response
