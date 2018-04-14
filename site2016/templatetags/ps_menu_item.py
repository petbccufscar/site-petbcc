from django import template
from django.utils.safestring import mark_safe
from ..models import ProcessoSeletivo

register = template.Library()


@register.simple_tag
def ps_menu():
    s = ""
    for ps in ProcessoSeletivo.objects.order_by('-data_inscricao_inicio'):
        s += '<a class="item" href="/processoseletivo/{0}/{1}">Processo Seletivo {0}/{1}</a>\n'.format(ps.ano,
                                                                                                       ps.semestre)
    return mark_safe(s)


@register.simple_tag
def ps_link_atual():
    ps = ProcessoSeletivo.objects.order_by('-data_inscricao_inicio')[0]

    s = '<a href="/processoseletivo/{0}/{1}">Processo Seletivo</a>\n'.format(ps.ano, ps.semestre)
    return mark_safe(s)
