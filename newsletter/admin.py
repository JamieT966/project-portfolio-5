from django.contrib import admin
from .models import NewsletterSubscriber
from import_export.admin import ExportActionMixin
from import_export import resources


class NewsletterExport(resources.ModelResource):

    class Meta:
        model = NewsletterSubscriber
        fields = 'signed_up_at, email,'


class NewsletterSubscriberAdmin(ExportActionMixin, admin.ModelAdmin):

    resource_class = NewsletterExport

    list_display = (
        'email',
        'signed_up_at',
    )

    ordering = ('-signed_up_at',)


admin.site.register(NewsletterSubscriber, NewsletterSubscriberAdmin)
