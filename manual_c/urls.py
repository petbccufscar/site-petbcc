from django.urls import path
from . import views

app_name = 'manual_c'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre/', views.sobre, name='sobre'),
    path('biblioteca/<str:biblioteca>/', views.biblioteca, name='biblioteca'),
]