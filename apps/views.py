from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.conf import settings

from django.template.loader import render_to_string

# Create your views here.
def index(request):

    if request.method ==   'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['asunto']
        mensaje = request.POST['mensaje']


        template = {

            'name': name,
            'email': email,
            'message':mensaje,
        }

        

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['olivares.wan@gmail.com']
        )
        email.fail_silently = False
        email.send()
        # return redirect('/contact/',template)

        return render(request, 'apps/contact.html', template)
    return render(request, 'apps/index.html')



def contact(request):
    return render(request, 'apps/contact.html')