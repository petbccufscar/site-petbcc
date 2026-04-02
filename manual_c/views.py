from django.shortcuts import render
from django.http import Http404

MODULES = [
    'assert', 'ctype', 'errno', 'float', 'limits', 'math', 'setjmp',
    'signal', 'stdarg', 'stdio', 'stdlib', 'string', 'time'
]

MODULES_MAP = {
    m: {
        'name': f'{m}.h',
        'h_template': f'manual_c/bibliotecas/{m}/{m}_h.html',  
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


def biblioteca(request, biblioteca):
    if biblioteca not in MODULES_MAP:
        raise Http404('Biblioteca não encontrada')

    return render(
        request,
        MODULES_MAP[biblioteca]['h_template'],
        context={
            'pagina': f'{biblioteca}_h',
        },
    )