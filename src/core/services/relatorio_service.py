from core.models import Pedido
from weasyprint import HTML
from django.template.loader import render_to_string

class RelatorioService:
    
    @staticmethod
    def _get_pedido(*, pedido_id,user):
        pedido = Pedido.objects.get(id=pedido_id)
        
        if  pedido.vendedor != user:
            raise PermissionError(
            "Pedido nao pertence ao vendedor"
            )
            
        return pedido
    
    @staticmethod
    def exportar_pedido_pdf(*, pedido_id,user):
        template_name = 'pedidos/pdf.html'
        pedido = RelatorioService._get_pedido(
            pedido_id=pedido_id,
            user=user
            )
    
        html_string = render_to_string(
            template_name,{
                'pedido':pedido
            }
        )
        pdf = HTML(string=html_string).write_pdf()
        
        return pdf
        
        
        
    """
    Reminder.
    Posso usar essas opçoes para gerar um pdf
    - reportLab
    - xhtml2pdf
    - weasyprint V
    - wkhtmltopdf
    - pdfkit
    """ 