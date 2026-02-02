from django.db import models
from django.contrib.auth.models import User

class Vendedor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
        )
    nome = models.CharField(max_length=255)
    documento = models.CharField(max_length=255, blank = True, null = True)
    telefone = models.CharField(max_length=20,blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    endereco = models.CharField(max_length=255,blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nome