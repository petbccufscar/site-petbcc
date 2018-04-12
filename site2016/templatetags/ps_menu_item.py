from django import template
from ..models import ProcessoSeletivo

register = template.Library()


@register.simple_tag
def ps_link():
    ps_atual = ProcessoSeletivo.objects.order_by('-data_inscricao_inicio').all()[0]
    return str(ps_atual.ano) + "/" + str(ps_atual.semestre)
