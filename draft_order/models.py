from django.db import models


class DraftOrder(models.Model):

    # product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=10)
    message = models.TextField(max_length=600) #If applicable
    created_at = models.DateTimeField(auto_now_add=True)