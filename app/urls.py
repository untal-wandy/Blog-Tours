from django.urls import path
from .views import *

app_name = 'app'
urlpatterns = [
    path('', index, name='index'),
    path('inicio/', inicio, name='inicio'),
    path('login/', login, name='login'),
    path('login_registrar/', login_registrar, name='login_registrar'),
    path('<int:paquete>/get_tours/', get_tours, name='get_tours'),


# paginas de administracion y usuario
    path('perfil/', perfil, name='perfil'),
    path('blog/', blog, name='blog'),
    path('faq/', faq, name='faq'),
    path('tours/', tours, name='tours'),
    path('admin_site/', admin_site, name='admin_site'),
]