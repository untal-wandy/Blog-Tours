from .views import *
from django.urls import path

app_name = 'apps'
urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),]

