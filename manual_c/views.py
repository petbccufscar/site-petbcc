from django.shortcuts import render
from django.http import Http404

MODULES = [
    'assert', 'ctype', 'errno', 'float', 'limits', 'math', 'setjmp',
    'signal', 'stdarg', 'stdio', 'stdlib', 'string', 'time'
]

MODULES_MAP = {
    m: {
        'name': f'{m}.h',
        'h_template': f'manual_c/libs/{m}/{m}_h.html',
        'funcoes_template': f'manual_c/libs/{m}/{m}_funcoes.html',
    }
    for m in MODULES
}


def inicio(request):
    return render(
        request,
        'manual_c/inicio.html',
        context={
            'modules': MODULES,
        },
    )


def sobre(request):
    return render(
        request,
        'manual_c/sobre.html',
        context={
            'modules': MODULES,
        },
    )


def modulo(request, modulo):
    if modulo not in MODULES_MAP:
        raise Http404('Biblioteca não encontrada')

    return render(
        request,
        MODULES_MAP[modulo]['h_template'],
        context={
            'pagina': f'{modulo}_h',
        },
    )


def modulo_funcoes(request, modulo):
    if modulo not in MODULES_MAP:
        raise Http404('Biblioteca não encontrada')

    return render(
        request,
        MODULES_MAP[modulo]['funcoes_template'],
        context={
            'pagina': f'{modulo}_funcoes',
        },
    )
