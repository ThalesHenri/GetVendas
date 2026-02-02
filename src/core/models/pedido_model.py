from django.db import models
from core.models import Cliente
from django.contrib.auth.models import User


class Pedido(models.Model):
    
    SATATUS_CHOICES= [
        ('RASCUNHO', 'Rascunho'),
        ('ENVIADO', 'Enviado'),
        ('FATURADO', 'Faturado'),
    ]
    
    vendedor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pedidos'
    )
    
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='pedidos'
    )
    
    status = models.CharField(
        max_length=20,
        choices=SATATUS_CHOICES,
        default='RASCUNHO'
    )
    
    total = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        default = 0
        )
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Pedido {self.id}'
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-criado_em']