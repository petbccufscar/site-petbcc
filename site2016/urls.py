from django.conf.urls import url
from site2016 import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^manutencao/$', views.manutencao, name='manutencao'),
    url(r'^equipe/$', views.equipe, name='equipe'),
    url(r'^equipe/(?P<id>[0-9]{1,3})/$', views.membro, name='membro'),
    url(r'^projetos/$', views.projetos, name='projetos'),
    url(r'^projetos/(?P<id>[0-9]{1,3})/$', views.projeto, name='projeto'),
    url(r'^processoseletivo/(?P<ano>[0-9]{4})/(?P<semestre>[0-9]{1})/$',
        views.processo_seletivo, name='processo_seletivo'),
    url(r'^contato/$', views.contato, name='contato'),

    # Manual C
    url(r'^manualc/$', views.manual_c, name='manual_c'),
    url(r'^sobre/$', views.sobre, name='sobre'),
    # Math.h
    url(r'^math/$', views.math_h, name='math_h'),
    url(r'^mathfuncoes/$', views.math_funcoes, name='math_funcoes'),
    # Assert.h
    url(r'^assert/$', views.assert_h, name='assert_h'),
    url(r'^assertfuncoes/$', views.assert_funcoes, name='assert_funcoes'),
    # Ctype.h
    url(r'^ctype/$', views.ctype_h, name='ctype_h'),
    url(r'^ctypefuncoes/$', views.ctype_funcoes, name='ctype_funcoes'),
    # Float.h
    url(r'^float/$', views.float_h, name='float_h'),
    # Setjmp.h
    url(r'^setjmp/$', views.setjmp_h, name='setjmp_h'),
    url(r'^setjmpfuncoes/$', views.setjmp_funcoes, name='setjmp_funcoes'),
    # Stdarg.h
    url(r'^stdarg/$', views.stdarg_h, name='stdarg_h'),
    # Stdio.h
    url(r'^stdio/$', views.stdio_h, name='stdio_h'),
    url(r'^stdiofuncoes/$', views.stdio_funcoes, name='stdio_funcoes'),
    # String.h
    url(r'^string/$', views.string_h, name='string_h'),
    url(r'^stringfuncoes/$', views.string_funcoes, name='string_funcoes'),
    # Errno.h
    url(r'^errno/$', views.errno_h, name='errno_h'),
    # Stdlib.h
    url(r'^stdlib/$', views.stdlib_h, name='stdlib_h'),
    url(r'^stdlibfuncoes/$', views.stdlib_funcoes, name='stdlib_funcoes'),
    # Time.h
    url(r'^time/$', views.time_h, name='time_h'),
    url(r'^timefuncoes/$', views.time_funcoes, name='time_funcoes'),
    # Limits.h
    url(r'^limits/$', views.limits_h, name='limits_h'),
    # Signal.h
    url(r'^signal/$', views.signal_h, name='signal_h'),
    url(r'^signalfuncoes/$', views.signal_funcoes, name='signal_funcoes'),
]
