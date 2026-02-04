from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def equipe(request):
    return render(request, 'core/equipe.html')

def projetos(request):
    return render(request, 'core/projetos.html')

def processo_seletivo(request):
    return render(request, 'core/processo_seletivo.html')

def contato(request):
    return render(request, 'core/contato.html')

def manual_c(request):
    return render(request, 'core/manual_c.html')