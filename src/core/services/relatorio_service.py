from core.models import Pedido

class RelatorioService:
    
    @staticmethod
    def get_pedido(*, pedido_id,user):
        pedido = Pedido.objects.get(id=pedido_id)
        
        if not pedido.vendedor != user:
            raise PermissionError(
            "Pedido nao pertence ao vendedor"
            )
            
        return pedido
    
    @staticmethod
    def exportar_pedido_pdf(*, pedido_id,user):
        pedido = RelatorioService.get_pedido(
            pedido_id=pedido_id,
            user=user
            )
        
        """
        Reminder.
        Posso usar essas opçoes para gerar um pdf
            - reportLab
            - xhtml2pdf
            - weasyprint
            - wkhtmltopdf
            - pdfkit
        """ 
                
        return pedido