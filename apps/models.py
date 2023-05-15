from django.db import models
from django import forms



class Payforms(forms.ModelForm):
      negocios = forms.CharField(max_length=100)
      cantidad = forms.CharField(max_length=10000)
      item_name = forms.CharField(max_length=100)
      facturea = forms.CharField(max_length=1000)
      notificacion = forms.CharField(max_length=100)
      returnar = forms.CharField(max_length=100)
      cancel_return = forms.CharField(max_length=100)
      custom = forms.CharField(max_length=100)
      

