from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied, ValidationError
from django.contrib.auth.models import User

from core.models import Vendedor


class AuthService:

    @staticmethod
    def login(*, request, username, password):
        """
        Autentica e loga o usuário no sistema.
        """
        user = authenticate(
            request=request,
            username=username,
            password=password
        )

        if not user:
            raise PermissionDenied('Usuário ou senha inválidos')

        if not user.is_active:
            raise PermissionDenied('Usuário inativo')

        login(request, user)
        return user

    @staticmethod
    def logout(*, request):
        """
        Realiza logout do usuário.
        """
        logout(request)
        
        
    @staticmethod
    def register(
            *, 
            username, 
            password, 
            nome, 
            telefone=None, 
            email=None, 
            documento=None, 
            endereco=None
        ):

        if User.objects.filter(username=username).exists():
            raise ValidationError('Usuário já existe')

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=nome
        )

        vendedor = Vendedor.objects.create(
            user=user,
            nome=nome,
            telefone=telefone,
            email=email,
            documento=documento,
            endereco=endereco
        )

        return vendedor
