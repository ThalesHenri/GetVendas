from core.models import Produto


class ProdutoService:
    
    @staticmethod
    def get_produtos_ativos():
        return Produto.objects.filter(ativo=True)
    
    @staticmethod
    def get_todos_produtos(user):
        # private de admin
        if not user.is_staff:
            raise PermissionError(
            'Este recurso é exclusivo para administradores'
            )
        return Produto.objects.all()
    
    @staticmethod
    def criar_produto(user, nome, sku, preco, imagem=None):
        if not user.is_staff:
            raise PermissionError(
            'Este recurso é exclusivo para administradores'
            )
        return Produto.objects.create(
            nome=nome,
            sku=sku,
            preco=preco,
            imagem=imagem
        )
        
    
    @staticmethod
    def desativar_produto(produto_id):
        protudo = Produto.objects.get(id=produto_id)
        protudo.ativo = False
        protudo.save()
        return protudo