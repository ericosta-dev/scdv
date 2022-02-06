from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    cpf = models.CharField(max_length=11,blank=True,null=True,unique=True) #Unique = Não deixa repetir no banco
    pass