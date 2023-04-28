from django.db import models
from django.contrib.auth.models import AbstractUser





class User(AbstractUser):
      paypal = models.CharField(max_length=100, blank=True)
      transferencia = models.CharField(max_length=100, blank=True)
      instagram = models.CharField(max_length=100, blank=True)
      facebook = models.CharField(max_length=100, blank=True)
      gmail = models.CharField(max_length=100, blank=True)





# TourUser reprenta que el usuario tiene que tener un Tour en su historial de viajes
class Tour_user_model(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      name = models.CharField(max_length=100, blank=True    )
      number_id_tour = models.IntegerField(default=0, blank=True)

      def __str__(self) -> int:
            return self.name



# Box of    models Tours
class Box_tours(models.Model):
      name_tour = models.CharField(max_length=100)
      code_paquet = models.CharField(max_length=100, blank=True)
      value_cu= models.CharField(max_length=100, blank=True)

      price = models.CharField(max_length=10)
      description = models.CharField(max_length=500)
      dia = models.CharField(max_length=100, default=False)

      photo = models.ImageField(upload_to="", blank=True, null=True)
      buy_getting = models.IntegerField(default=0, blank=True)
      reserved_getting = models.IntegerField(default=0, blank=True)

      cupos = models.CharField(max_length=100, blank=True)
      limites = models.CharField(max_length=100, blank=True)

      def __str__(self) -> str:
            return self.name_tour
      

