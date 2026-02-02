from core.models import Pedido, PedidoItem, Produto,Cliente
from django.db import transaction
from django.db.models import Sum

#coracao da aplicação

class PedidoService:
    
    @staticmethod
    @transaction.atomic
    def criar_pedido(*,vendedor,cliente_id,itens):
        """
        Presume-se que itens chegue neste formato
        
        itens = [
            {"produto_id": 1, "quantidade": 2},
            {"produto_id": 2, "quantidade": 3},   
        ]
        """
        cliente = Cliente.objects.get(id=cliente_id)
        
        #Check Segurança
        if cliente.vendedor != vendedor:
            raise PermissionError('Cliente nao pertence ao vendedor')
        
        pedido = Pedido.objects.create(
            vendedor=vendedor,
            cliente=cliente
        )
        
        total = 0
        for item in itens:
            produto = Produto.obects.get(
                id=item["produto_id"],
                ativo=True
            )
            
            quantidade = int(item["quantidade"])
            
            PedidoItem.objects.create(
                pedido = pedido,
                produto = produto,
                quantidade = quantidade,
                preco_unitario = produto.preco
            )
            
            total += produto.preco * quantidade
            
        pedido.total = total
        pedido.save()
        
        return pedido
    
    
    @staticmethod
    def get_pedidos_por_vendedor(vendedor):
        return Pedido.objects.filter(vendedor=vendedor)

        
    @staticmethod
    def get_pedidos(user):
        # private de admin
        if not user.is_staff:
            raise PermissionError(
            'Este recurso é exclusivo para administradores'
            )
        return Pedido.objects.all()
    
    
    @staticmethod
    def get_pedido_por_id(*, pedido_id, vendedor):
        pedido =  Pedido.objects.get(id=pedido_id)
        
        if pedido.vendedor != vendedor:
            raise PermissionError('Pedido nao pertence ao vendedor')
        
        return pedido
    

    @staticmethod
    def faturar_pedido(pedido_id):
        pedido = Pedido.objects.get(id=pedido_id)
        pedido.status = 'FATURADO'
        pedido.save()
        return pedido
    
    
    def total_vendido_por_vendedor(vendedor):
        return (
            Pedido.objects
            .filter(vendedor=vendedor)
            .aggregate(Sum('total'))['total__sum']
            or 0
        )    