from core.models import Cliente

class ClienteService:
    
    @staticmethod
    def get_clientes_por_vendedor(vendedor):
        return Cliente.objects.filter(vendedor=vendedor)
    
    def criar_cliente(*, vendedor, nome, telefone,documento=None, email=None, endereco=None):
        return Cliente.objects.create(
            vendedor=vendedor,
            nome=nome,
            documento=documento,
            telefone=telefone,
            email=email,
            endereco=endereco
        )
        
    def get_cliente_por_id(*, cliente_id, vendedor):
        cliente =  Cliente.objects.get(id=cliente_id)
        
        if cliente.vendedor != vendedor:
            raise PermissionError('Cliente nao pertence ao vendedor')
        
           
        return cliente