from django.db import models

class PedidoItem(models.Model):
    pedido = models.ForeignKey(
        'Pedido', on_delete=models.CASCADE, 
        related_name='itens'
        )
    produto = models.ForeignKey(
        'Produto', 
        on_delete=models.PROTECT
        )
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(
        max_digits=10, 
        decimal_places=2
        )
    criado_em = models.DateTimeField(auto_now_add=True)
    
    @property
    def subtotal(self):
        return self.quantidade * self.preco_unitario
    
    def __str__(self):
        return super().__str__()