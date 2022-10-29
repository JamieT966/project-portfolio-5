from django.db import models
from products.models import Product
from django.template.defaultfilters import truncatewords


class ContactForm(models.Model):
    """
    Allows user to contact store by filling out contact form.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    product = models.ForeignKey(
        Product,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    message = models.TextField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def short_message(self):
        return truncatewords(self.message, 12)

    def __str__(self):
        return self.name
