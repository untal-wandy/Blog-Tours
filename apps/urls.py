from .views import *
from django.urls import path

app_name = 'apps'
urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('es/', inicio, name='inicio'),
    path(' paypal-ipn/', paypal_ipn ,name=' paypal-ipn'),
    path('paypal-cancel/', paypal_cancel ,name='paypal-cancel'),
    path('paypal-reverse/', paypal_reverse, name='paypal-reverse'),
    ]



