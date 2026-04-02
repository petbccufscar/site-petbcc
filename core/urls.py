from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('equipe', views.equipe, name='equipe'),
    path('projetos', views.projetos, name='projetos'),
    path('processo-seletivo', views.processo_seletivo, name='processo-seletivo'),
    path('contato', views.contato, name='contato')
]