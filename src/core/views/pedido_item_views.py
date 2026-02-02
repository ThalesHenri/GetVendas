from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib import messages

from core.models import Cliente, Pedido, Produto
from core.services import PedidoService
from core.services import PedidoItemService


class PedidoCreateView(LoginRequiredMixin, View):

    template_name = 'pedidos/novo_pedido.html'

    def get(self, request):
        clientes = Cliente.objects.filter(vendedor=request.user)
        return render(request, self.template_name, {'clientes': clientes})
    def post(self, request):
        id_cliente = request.POST.get('cliente')
        cliente = get_object_or_404(
            Cliente,
            id=id_cliente,
            vendedor=request.user
        )

        pedido = PedidoService.criar_pedido_vazio(
            vendedor=request.user,
            cliente_id=id_cliente
        )

        return redirect('pedido_itens', pedido_id=pedido.id)


class PedidoItensView(LoginRequiredMixin, View):

    template_name = 'pedidos/pedido_itens.html'
    def get(self, request, pedido_id):
        pedido = get_object_or_404(
            Pedido,
            id=pedido_id,
            vendedor=request.user
        )

        produtos = Produto.objects.filter(ativo=True)
        return render(request, self.template_name, {'pedido': pedido, 'produtos': produtos})

        

    def post(self, request, pedido_id):
        pedido = get_object_or_404(
            Pedido,
            id=pedido_id,
            vendedor=request.user
        )

        produto_id = request.POST.get('produto')
        quantidade = int(request.POST.get('quantidade', 1))

        try:
            PedidoItemService.adicionar_item(
                pedido=pedido,
                produto_id=produto_id,
                quantidade=quantidade
            )
            messages.success(request, 'Item adicionado com sucesso')

        except Exception as e:
            messages.error(request, str(e))

        return redirect('pedido_itens', pedido_id=pedido.id)
