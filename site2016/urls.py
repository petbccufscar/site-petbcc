from django.conf.urls import url
from site2016 import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^manutencao/$', views.manutencao, name='manutencao'),
    url(r'^equipe/$', views.equipe, name='equipe'),
    url(r'^projetos/$', views.projetos, name='projetos'),
    # url(r'^noticias/$', views.noticias, name='noticias'),
    url(r'^sobre/$', views.sobre, name='sobre'),
    url(r'^processoseletivo/$', views.processo_seletivo, name='processo_seletivo'),
    url(r'^contato/$', views.contato, name='contato'),
]
