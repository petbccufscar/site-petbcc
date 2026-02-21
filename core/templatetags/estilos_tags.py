from django import template

register = template.Library()

@register.filter
def estilo_categoria(categoria):
    cores = {
        "ensino": "bg-blue-500 text-gray-50",
        "pesquisa": "bg-green-500 text-gray-50",
        "extensao": "bg-purple-500 text-gray-50",
        "desenvolvimento": "bg-orange-500 text-gray-50",
        "marketing": "bg-blue-200 text-gray-50",
        "financeiro": "bg-teal-500 text-gray-50",
        "administrativo": "bg-gray-500 text-gray-50",
        "gestao-de-pessoas": "bg-pink-500 text-gray-50",
    }
    
    return cores.get(str(categoria).lower(), "bg-white text-gray-800 border-gray-200 border")

@register.filter
def estilo_status_projeto(categoria):
    cores = {
        "ativo": "bg-green-600 text-white",
        "suspenso": "bg-orange-500 text-white",
        "planejamento": "bg-gray-100 text-gray-400",
        "finalizado": "bg-green-500 text-white",
    }
    
    return cores.get(str(categoria).lower(), "bg-white text-gray-800 border-gray-200 border")