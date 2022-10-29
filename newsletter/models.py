from django.db import models


class NewsletterSubscriber(models.Model):
    """
    Newsletter sign up model
    """
    email = models.EmailField()
    signed_up_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
