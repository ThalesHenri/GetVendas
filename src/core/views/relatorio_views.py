from django.views import View
from django.http import HttpResponse,Http404
from django.contrib.auth.mixins import LoginRequiredMixin

from core.services import RelatorioService

class RelatorioView(LoginRequiredMixin, View):
    def get(self, request, pedido_id):
        try: 
            pdf = RelatorioService.exportar_pedido_pdf(
                pedido_id=pedido_id,
                user=request.user
            )        
        except PermissionError:
            raise Http404("Pedido não encontrado")
        
        response = HttpResponse(
                pdf, 
                content_type='application/pdf'
            )
        response['Content-Disposition'] = f'inline; filename="pedido-{pedido_id}.pdf"'
        return response