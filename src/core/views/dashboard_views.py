from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from core.services import DashboardService
from django.views import View

class DashboardView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = request.user

        if user.is_staff:
            context = DashboardService.dashboard_central()
            template_name = 'dashboard/dashboard_central.html'
        else:
            context = DashboardService.dashboard_vendedor(user)
            template_name = 'dashboard/dashboard_vendedor.html'

        return render(request, template_name, context)