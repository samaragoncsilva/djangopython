from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    telefone=models.CharField(max_length=20,blank=True,null=True)
    # Adicione campos extras aqui, se quiser
    pass

