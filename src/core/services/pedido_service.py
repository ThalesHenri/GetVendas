from django.db import transaction, models
from django.db.models import Sum

from core.models import Pedido, PedidoItem, Produto, Cliente

#coração do projeto
class PedidoService:
  
    @staticmethod
    @transaction.atomic
    def criar_pedido_vazio(*, vendedor, cliente_id):
        
        cliente = Cliente.objects.get(id=cliente_id)

        # Segurança
        if cliente.vendedor != vendedor:
            raise PermissionError('Cliente não pertence ao vendedor')

        pedido = Pedido.objects.create(
            vendedor=vendedor,
            cliente=cliente,
            status='RASCUNHO',
            total=0
        )

        return pedido

    @staticmethod
    def get_pedidos_por_vendedor(vendedor):
        return Pedido.objects.filter(vendedor=vendedor)

    @staticmethod
    def get_pedidos(user):
        # exclusivo admin
        if not user.is_staff:
            raise PermissionError(
                'Este recurso é exclusivo para administradores'
            )
        return Pedido.objects.all()

    @staticmethod
    def get_pedido_por_id(*, pedido_id, vendedor):
        pedido = Pedido.objects.get(id=pedido_id)

        if pedido.vendedor != vendedor:
            raise PermissionError('Pedido não pertence ao vendedor')

        return pedido

    @staticmethod
    @transaction.atomic
    def faturar_pedido(*, pedido_id, vendedor):
        pedido = Pedido.objects.select_for_update().get(id=pedido_id)

        if pedido.vendedor != vendedor:
            raise PermissionError('Pedido não pertence ao vendedor')

        if pedido.status != 'RASCUNHO':
            raise ValueError('Apenas pedidos em rascunho podem ser faturados')

        pedido.status = 'FATURADO'
        pedido.save(update_fields=['status'])

        return pedido

    @staticmethod
    def total_vendido_por_vendedor(vendedor):
        return (
            Pedido.objects
            .filter(vendedor=vendedor, status='FATURADO')
            .aggregate(Sum('total'))['total__sum']
            or 0
        )

    @staticmethod
    def recalcular_total(pedido):
      
        total = (
            pedido.itens
            .aggregate(
                total=Sum(
                    models.F('quantidade') * models.F('preco_unitario')
                )
            )['total']
            or 0
        )

        pedido.total = total
        pedido.save(update_fields=['total'])

        return total


