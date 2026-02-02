from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    vendedor = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='clientes'
        )
    nome = models.CharField(max_length=255)
    documento = models.CharField(max_length=255, blank = True, null = True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    endereco = models.CharField(max_length=255)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome    