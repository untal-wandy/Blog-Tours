from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
# from email import MIMEText
from smtplib import SMTP

from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string


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