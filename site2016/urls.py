from django.conf.urls import url
from site2016 import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^manutencao/$', views.manutencao, name='manutencao'),
    url(r'^equipe/$', views.equipe, name='equipe'),
    url(r'^projetos/$', views.projetos, name='projetos'),
    url(r'^processoseletivo/$', views.processo_seletivo, name='processo_seletivo'),
    url(r'^processoseletivo/2017/1/$', views.processo_seletivo_2017_1, name='processo_seletivo_2017_1'),
    url(r'^contato/$', views.contato, name='contato'),
]
