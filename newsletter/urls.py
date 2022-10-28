from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.display_newsletter_fom, name='newsletter'),
    path('unsubscribe/', views.unsubcribe_newsletter, name='unsubscribe'),
    path('export/<str:format>/', views.export_newsletter, name='export'),
]
