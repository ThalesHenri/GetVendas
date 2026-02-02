from django.urls import path
from .views import * 

urlpatterns = [
    path('', LandingPage.as_view(), name='landing'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    path('dashboard/', DashboardView.as_view(), name='dashboard')
]