from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.exceptions import PermissionDenied

from core.services.auth_service import AuthService

from django.core.exceptions import ValidationError



class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            AuthService.login(
                request=request,
                username=username,
                password=password
            )
            return redirect('dashboard')

        except PermissionDenied as e:
            messages.error(request, str(e))
            return render(request, self.template_name)


class LogoutView(View):

    def get(self, request):
        AuthService.logout(request=request)
        return redirect('login')


class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponse('Voce ja esta logado')
        return render(request, self.template_name)

    def post(self, request):
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        documento = request.POST.get('documento')
        endereco = request.POST.get('endereco')
        
        if password != password_confirm:
            messages.error(request, 'As senhas não conferem')
            return render(request, self.template_name)
        
      


        try:
            AuthService.register(
                username=username,
                nome=nome,
                documento=documento,
                endereco=endereco,
                telefone=telefone,
                email=email,
                password=password
            )
            messages.success(request, 'Conta criada com sucesso. Faça login.')
            return redirect('login')

        except ValidationError as e:
            messages.error(request, e.message)
            return render(request, self.template_name)