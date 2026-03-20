from django import template

register = template.Library()

@register.filter
def icone_categoria(categoria):
    icones = {
        "ensino": "book-outline",
        "pesquisa": "bulb-outline",
        "extensao": "earth-outline",
        "desenvolvimento-de-software": "code-slash-outline",
        "marketing": "megaphone-outline",
        "financeiro": "cash-outline",
        "administrativo": "mail-outline",
        "gestao-de-pessoas": "people-circle-outline",
    }
    
    return icones.get(str(categoria).lower(), "briefcase-outline")

