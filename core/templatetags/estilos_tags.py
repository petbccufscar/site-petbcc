from django import template

register = template.Library()


@register.filter
def estilo_botao(estilo):
    estilos = {
        "outline": "transition border border-blue-500 text-blue-500",
        "outline-white": "transition border border-cyan-50 text-cyan-50 hover:bg-cyan-50 hover:text-gray-800",
        "white": "transition border border-cyan-50 text-gray-800 bg-cyan-50 hover:bg-cyan-100",
        "white-outline": "transition border border-cyan-50 text-gray-800 bg-cyan-50 hover:bg-transparent hover:text-cyan-50"
    }
    
    return estilos.get(str(estilo).lower(), "transition border border-cyan-500 bg-cyan-500 text-gray-50 hover:bg-cyan-600")

@register.filter
def estilo_categoria(categoria, extra=None):
    cores = {
        "ensino": "bg-blue-500 text-gray-50",
        "pesquisa": "bg-green-500 text-gray-50",
        "extensao": "bg-red-500 text-gray-50",
        "desenvolvimento": "bg-orange-500 text-gray-50",
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
    }
    
    return cores.get(str(categoria).lower(), "bg-white text-gray-800 border-gray-200 border") + (" " + extra if extra else "")