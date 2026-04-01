from django.urls import path
from . import views

app_name = 'manual_c'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre/', views.sobre, name='sobre'),
    path('biblioteca/<str:modulo>/', views.modulo, name='biblioteca'),
    path('biblioteca/<str:modulo>/funcoes/', views.modulo_funcoes, name='biblioteca_funcoes'),
]