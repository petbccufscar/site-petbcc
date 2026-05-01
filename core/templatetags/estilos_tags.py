from django import template

register = template.Library()

@register.filter
def estilo_categoria(categoria, extra=None):
    cores = {
        "ensino": "bg-blue-500 text-gray-50",
        "pesquisa": "bg-green-500 text-gray-50",
        "extensao": "bg-red-500 text-gray-50",
        "desenvolvimento-de-software": "bg-orange-500 text-gray-50",
        "marketing": "bg-blue-200 text-gray-50",
        "financeiro": "bg-teal-500 text-gray-50",
        "administrativo": "bg-gray-500 text-gray-50",
        "gestao-de-pessoas": "bg-pink-500 text-gray-50",
    }
    
    return cores.get(str(categoria).lower(), "bg-white text-gray-800 border-gray-200 border") + (" " + extra if extra else "")

@register.filter
def estilo_status_projeto(categoria, extra=None):
    cores = {
        "ativo": "bg-yellow-500 text-white",
        "suspenso": "bg-gray-100 text-gray-500",
        "planejamento": "bg-purple-500 text-white ",
        "finalizado": "bg-green-600 text-white",
        "desenvolvimento": "bg-yellow-500 text-white"
    }
    
    return cores.get(str(categoria).lower(), "bg-white text-gray-800 border-gray-200 border") + (" " + extra if extra else "")

@register.filter
def estilo_badge(categoria, extra=None):
    cores = {
        "cyan": "bg-cyan-500 text-white text-sm",
    }
    
    return cores.get(str(categoria).lower(), "bg-white text-gray-800 border-gray-200 border") + (" " + extra if extra else "")