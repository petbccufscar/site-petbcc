def menu_items(request):
  current = request.resolver_match.view_name if request.resolver_match else ""

  def is_active(route_name):
    return route_name in current

  return {
    "menu_items": [
      {
        "label": "Início",
        "route": "core:inicio",
        "active": is_active("core:inicio"),
      },
      {
        "label": "Equipe",
        "route": "core:equipe",
        "active": is_active("core:equipe"),
      },
      {
        "label": "Projetos",
        "route": "core:projetos",
        "active": is_active("core:projetos"),
      },
      {
        "label": "Processo Seletivo",
        "route": "core:processo-seletivo",
        "active": is_active("core:processo-seletivo"),
      },
      {
        "label": "Contato",
        "route": "core:contato",
        "active": is_active("core:contato"),
      },
      {
        "label": "Manual C",
        "route": "manual_c:inicio",
        "active": is_active("manual_c"),
      },
    ]
  }
