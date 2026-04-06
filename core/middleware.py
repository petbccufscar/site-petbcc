# core/middleware.py
from django.shortcuts import render
from django.conf import settings

class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # evita loop infinito na própria página de manutenção
        if settings.MAINTENANCE_MODE:
            if request.user.is_staff:
                return self.get_response(request)
        
            if request.path != "/manutencao/":
                return render(request, "core/manutencao.html", status=503)

        return self.get_response(request)