from django.contrib import admin
from .models import NewsletterSubscriber

class NewsletterSubscriberAdmin(admin.ModelAdmin):

    list_display = (
        'email',
        'signed_up_at',
    )

    ordering = ('-signed_up_at',)

admin.site.register(NewsletterSubscriber ,NewsletterSubscriberAdmin)
