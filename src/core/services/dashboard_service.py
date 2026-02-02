from django.db.models import Sum, Count
from core.models import Pedido


class DashboardService:
    
    
    @staticmethod
    def dashboard_vendedor(user):
        pedidos = Pedido.objects.filter(vendedor=user)
        total_pedidos = pedidos.count() 
        rascunhos = pedidos.filter(status='RASCUNHO').count()
        enviados = pedidos.filter(status='ENVIADO').count()
        faturados = pedidos.filter(status='FATURADO').count()
        total_faturado = pedidos.filter(
            status='FATURADO'
        ).aggregate(total=Sum('total'))['total'] or 0
        ultimos_pedidos = pedidos[:10]
        data = {
            'total_pedidos': total_pedidos,
            'rascunhos': rascunhos,
            'enviados': enviados,
            'faturados': faturados,
            'total_faturado': total_faturado,
            'ultimos_pedidos': ultimos_pedidos
        }
        return data

    @staticmethod
    def dashboard_central():
        pedidos = Pedido.objects.all()
        total_pedidos = pedidos.count() 
        rascunhos = pedidos.filter(status='RASCUNHO').count()
        enviados = pedidos.filter(status='ENVIADO').count()
        faturados = pedidos.filter(status='FATURADO').count()
        total_faturado = pedidos.filter(
            status='FATURADO'
        ).aggregate(total=Sum('total'))['total'] or 0
        ultimos_pedidos = pedidos[:10]
        data = {
            'total_pedidos': total_pedidos,
            'rascunhos': rascunhos,
            'enviados': enviados,
            'faturados': faturados,
            'total_faturado': total_faturado,
            'ultimos_pedidos': ultimos_pedidos
        }
        
        return data