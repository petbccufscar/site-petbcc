def menu_items_manual_c(request):
    current_url = request.resolver_match.url_name if request.resolver_match else ""
    biblioteca_atual = request.resolver_match.kwargs.get("biblioteca", "") if request.resolver_match else ""

    principal = [
        {
            "label": "Início",
            "route": "manual_c:inicio",
            "active": current_url == "inicio",
        },
        {
            "label": "Sobre",
            "route": "manual_c:sobre",
            "active": current_url == "sobre",
        },
    ]

    bibliotecas = [
        "assert",
        "ctype",
        "errno",
        "float",
        "limits",
        "math",
        "setjmp",
        "signal",
        "stdarg",
        "stdio",
        "stdlib",
        "string",
        "time",
    ]

    bibliotecas_menu = [
        {
            "nome": b,
            "active": b == biblioteca_atual,
        }
        for b in bibliotecas
    ]

    return {
        "menu_manual_c": {
            "principal": principal,
            "bibliotecas": bibliotecas_menu,
        }
    }