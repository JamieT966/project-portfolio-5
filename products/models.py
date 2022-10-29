from django.db import models
from ckeditor.fields import RichTextField
from profiles.models import UserProfile
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg

RATING_OPTIONS = (
    (0, '0'),
    (0.5, '0.5'),
    (1, '1'),
    (1.5, '1.5'),
    (2, '2'),
    (2.5, '2.5'),
    (3, '3'),
    (3.5, '3.5'),
    (4, '4'),
    (4.5, '4.5'),
    (5, '5'),
    )


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        null=True, blank=True,
        on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = RichTextField(blank=True, null=True)
    has_sizes = models.BooleanField(null=True, blank=True, default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    # Advised by my mentor Brian Macharia on how to have this work
    def rating(self):
        reviews = Review.objects.filter(
            product=self,
            status='True').aggregate(avarage=Avg('rating'))
        avg = 0
        if reviews["avarage"] is not None:
            avg = float(reviews["avarage"])
        return round(avg, 2)


class Review(models.Model):
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='reviews')
    product = models.ForeignKey(
        Product, null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='reviews')
    title = models.CharField(max_length=50, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField(
        choices=RATING_OPTIONS, default=5,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
