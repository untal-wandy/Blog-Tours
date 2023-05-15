import smtplib
from email.mime.text import MIMEText
# from email import MIMEText
from smtplib import SMTP
from django.urls import reverse
from django.conf import settings
from django.shortcuts import redirect, render 
from paypal.standard.forms import PayPalPaymentsForm
from django import forms
import uuid

import requests

headers = {
    'Content-Type': 'application/json',
    'PayPal-Request-Id': '7b92603e-77ed-4896-8e78-5dea2050476a',
    'Authorization': 'Bearer 6V7rbVwmlM1gFZKW_8QtzWXqpcwQ6T5vhEGYNJDAAdn3paCgRpdeMdVYmWzgbKSsECednupJ3Zx5Xd-g',
}

data = '{ "intent": "CAPTURE", "purchase_units": [ { "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b", "amount": { "currency_code": "USD", "value": "100.00" } } ], "payment_source": { "paypal": { "experience_context": { "payment_method_preference": "IMMEDIATE_PAYMENT_REQUIRED", "payment_method_selected": "PAYPAL", "brand_name": "EXAMPLE INC", "locale": "en-US", "landing_page": "LOGIN", "shipping_preference": "SET_PROVIDED_ADDRESS", "user_action": "PAY_NOW", "return_url": "https://example.com/returnUrl", "cancel_url": "https://example.com/cancelUrl" } } } }'

response = requests.post('https://api-m.sandbox.paypal.com/v2/checkout/orders', headers=headers, data=data)


class ContactForm(forms.Form):
      negocios = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Negocios'}) )
      cantidad = forms.CharField(max_length=10000, widget=forms.TextInput(attrs={'placeholder': 'Cantidad'}) )
      item_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre del item'}) )
      facturea = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'placeholder': 'Factura'}))
      notificacion = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Notficificacion'}))
      returnar = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Returnar'}))
      cancel_return = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Cancelar'}))
      custom = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Custom'}))
      

# Create your views here.
def index(request):

    if request.method ==   'POST':
        name = request.POST.get('name', ' ')
        email = request.POST.get('email', ' ')
        subject = request.POST.get('subject', ' ')
        mensaje = request.POST.get('mensaje', ' ')


        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        mailServer.ehlo()
        print(mailServer.ehlo())
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(settings.EMAIL_USER, settings.EMAIL_HOTS_PASSWORD)
        print("Conectado")


        mensaje = MIMEText("""Este es el mensaje
        de las narices creado por Wandy Olivares""")
        mensaje['From']= settings.EMAIL_HOST
        mensaje['To']= 'wnady.olivares@gmail.com'
        mensaje['Subject']="Tienes un correo"

        # Envio del mensaje
        mailServer.sendmail(settings.EMAIL_HOST,
                        "olivares.wan@gmail.com",
                        mensaje.as_string())
        print('Correo enviado')

        # send = send_mail (
        #     name, mensaje, email,
        #     ['olivares.wan@gmail.com'],
        #     fail_silently=False,
        # )

        # try:
        #     server = smtplib.SMTP('smtp.gmail.com', 587)
        #     server.ehlo()
        # except:
        #     print('Something went wrong...')

        template = {
            'name': name,
            'email': email,
            'message':mensaje,  }

        # email = EmailMessage( 
        #     'Mensaje recivido',
        #     'Mensaje recivido por: Wandy Olivares: '.format(name, email, mensaje),
        #     email,
        #     ['olivares.wan@gmail.com']
        # )
        # email.send()

        # return redirect('/contact/',template)

        return render(request, 'apps/contact.html', template)
    return render(request, 'apps/index.html')



def contact(request):
    return render(request, 'apps/contact.html')


def inicio(request):
    PAYPAL_RECEIVER_EMAIL  = 'sb-easix25999816@business.example.com'
    pago = 21

    paypal_dict = {
        "business": PAYPAL_RECEIVER_EMAIL,
        "amount": pago ,
        "item_name": "El sol del la mirada",
        "invoice": str(uuid.uuid4()),
        "currency_code": "USD",
        "notify_url": "" ,
        "return": '' ,
        "cancel_return": "",
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}    
    return render(request, 'apps/inicio.html', context )


def paypal_ipn(request):
    return redirect('/apps/es/')

def paypal_cancel(request):
    return redirect('/apps/es/')

def paypal_reverse(request):
    return redirect('/apps/es/')