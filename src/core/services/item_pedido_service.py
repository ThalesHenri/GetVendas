from core.models import Pedido, Produto, PedidoItem
from django.core.exceptions import ValidationError

class PedidoItemService:

    @staticmethod
    def adicionar_item(*, pedido, produto_id, quantidade):
        if pedido.status != 'RASCUNHO':
            raise ValidationError('Pedido não pode ser alterado')

        produto = Produto.objects.get(id=produto_id)

        item = PedidoItem.objects.create(
            pedido=pedido,
            produto=produto,
            quantidade=quantidade,
            preco_unitario=produto.preco
        )

        PedidoItemService.recalcular_total(pedido)
        return item

    @staticmethod
    def remover_item(item_id):
        item = PedidoItem.objects.get(id=item_id)
        pedido = item.pedido

        if pedido.status != 'RASCUNHO':
            raise ValidationError('Pedido não pode ser alterado')

        item.delete()
        PedidoItemService.recalcular_total(pedido)

    @staticmethod
    def recalcular_total(pedido):
        total = sum(item.subtotal for item in pedido.itens.all())
        pedido.total = total
        pedido.save()
