from django.urls import path
from .views import * 

urlpatterns = [
    path('', LandingPage.as_view(), name='landing'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('pedidos/', PedidoCreateView.as_view(), name='pedidos'),
    path('pedidos/novo/', PedidoCreateView.as_view(), name='novo_pedido'),
    path('pedidos/<int:pedido_id>/itens/',PedidoItensView.as_view(),name='pedido_itens'),
    path('pedidos/<int:pedido_id>/pdf/',RelatorioView.as_view(),name='pedido_pdf'),
    
    path('clientes/', ClienteView.as_view(), name='clientes'),
    path('clientes/novo/', ClienteView.as_view(), name='novo_cliente'),
]