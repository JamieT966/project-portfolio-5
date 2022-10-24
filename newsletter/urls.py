from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.display_newsletter_fom, name='newsletter'),
    path('unsubcribe/', views.unsubcribe_newsletter, name='unsubcribe'),
]
