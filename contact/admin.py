from django.contrib import admin
from .models import ContactForm


class ContactFormAdmin(admin.ModelAdmin):

    list_display = (
        'created_at',
        'name',
        'email',
        'phone',
        'product',
        'short_message',
    )

    ordering = ('-created_at',)


admin.site.register(ContactForm, ContactFormAdmin)
