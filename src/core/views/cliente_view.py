from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from core.models import Cliente
from core.services.cliente_service import ClienteService
from django.contrib import messages


class ClienteView(LoginRequiredMixin, View):
    
    template_name = 'clientes/novo_cliente.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        try:
            ClienteService.criar_cliente(
            vendedor=request.user,
            nome=request.POST.get('nome'),
            documento=request.POST.get('documento'),
            telefone=request.POST.get('telefone'),
            email=request.POST.get('email'),
            endereco=request.POST.get('endereco'),
        )
            messages.success(request, 'Cliente criado com sucesso')
            return redirect('novo_pedido')

        except Exception as e:
            messages.error(request, str(e))
            return render(request, self.template_name)
            