from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  logout
from django.contrib.auth.models import User
from .models import *


def login_registrar(request):

    if request.method == 'POST':
        user = User()
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            error_message = "Las contraseñas no coinciden"
            print(error_message)
            return render(request,'registration/login_registrar.html', {'error': error_message})
        print('Las contraseñas coinciden')

        email = request.POST['email']
        first_name = request.POST['first_name']

        if User.objects.filter(username=username).exists():
            user_exists_error_message = "Este usuario ya existe"    
            return render(request,'registration/login_registrar.html', {'error': 'Usuario o contraseña incorrectos'})
        
        else:
            user.username = username
            user.email = email
            user.first_name = first_name
            user.set_password(password)
            user.save()
            return redirect('/inicio/')
        
    return render(request, 'registration/login_registrar.html')




def index(request):
    return render(request, 'app/index.html')

@login_required
def inicio(request):
    return render(request, 'app/inicio.html')


def login(request):
    logout(request)
    return redirect('/')




@login_required
def get_tours(request, paquete):
        
        
    box_tours = Box_tours.objects.filter(id=paquete)
    user_get_paquet = User.objects.get(id=request.user.id)
    tours = Box_tours.objects.filter(id=paquete) 
    save = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        asientos = request.POST.get("asientos")
        if asientos is not None:
                listo = int(asientos)
                number_asientos = int

                delete_a_asientos = Box_tours.objects.filter(id=paquete)
                for asientos in delete_a_asientos:
                    number_asientos =  asientos.asientos
                    print(number_asientos)

                if number_asientos <= 0:
                    for asientos in delete_a_asientos:
                        asientos.asientos = 0
                        asientos.save()
                else:
                    for asientos in delete_a_asientos:
                     asientos.asientos = number_asientos -listo
                    asientos.save()
                        # else:
                        #      print('es igual a 0')


                get_buy_tours =  Box_tours.objects.filter(id=paquete) 
                for buy in get_buy_tours:
                        buys = buy.get_buy_tours_set.create(number_get_buy=1)
                        # print(buys)

                for tour in tours:
                        get_paquet = save.tour_user_model_set.create(name=tour.name_tour, number_id_tour=paquete)
                        messeje_get_buy = 'Adquerido su Tour', tour.name_tour
                        # print(messeje_get_buy)
    return render(request, 'app/get_tours.html',  {'box_tours': box_tours})




def blog(request):
    post = Blog.objects.all()

    return render(request, 'app/blog.html', {'post': post})




def faq(request):
    faq = Faq.objects.all()
    return render(request, 'app/faq.html', {'faq': faq})




@login_required
def tours(request): 
    if request.user.is_authenticated:
        print(request.user.id)
    else:
        print('No hay nadie autenticaco en este momento')

    box_tours = Box_tours.objects.all()
    return render(request, 'app/tours.html', {'box_tours': box_tours})




@login_required
def perfil(request):

    if request.user.is_authenticated:
        # user_registrado verifica que el usuario esta logueado
        user_registrado = User.objects.get(pk=request.user.id)
        # user hace se usa para identificar el usuario para buscar la llave foranea
        user = User.objects.filter(pk=request.user.id)
        # tours_getting obtiene el historial de tours de ese usuario
        tours_getting = user_registrado.tour_user_model_set.all()

        print(request.user.id, user_registrado)

        # from django.core.mail import send_mail

        # send_mail(
        #     "Subject here",
        #     "Here is the message.",
        #     "wandy.oli@icloud.com",
        #     ["wandy.oli@icloud.com"],
        #     fail_silently=False,)
        

    else:
        print('No hay nadie autenticado en este momento')

    return render(request, 'app/perfil.html', 
                  {'user': user,
                   'tours_getting':tours_getting},)










@login_required
def admin_site(request):
    return render(request, 'app/admin_site.html')