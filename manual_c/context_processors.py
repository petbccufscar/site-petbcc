def menu_items_manual_c(request):
    current_url = request.resolver_match.url_name if request.resolver_match else ""
    current_modulo = request.resolver_match.kwargs.get("biblioteca", "") if request.resolver_match else ""

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

    modulos = [
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

    modulos_menu = [
        {
            "nome": m,
            "active": m in current_modulo,
        }
        for m in modulos
    ]

    return {
        "menu_manual_c": {
            "principal": principal,
            "modulos": modulos_menu,
        }
    }