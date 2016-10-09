from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'site2016/home.html', {})


def equipe(request):
    return render(request, 'site2016/equipe.html', {})

def projetos(request):
    return render(request, 'site2016/projetos.html', {})

def exemplo_foundation(request):
    return render(request, 'site2016/ExemplosFoundation/index.html', {})