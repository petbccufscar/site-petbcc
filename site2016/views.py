from django.shortcuts import render

# Create your views here.

def home(request):
    context_dictionary = {'pagina': 'home'}
    return render(request, 'site2016/home.html', context_dictionary)

def equipe(request):
    context_dictionary = {'pagina': 'equipe'}
    return render(request, 'site2016/equipe.html', context_dictionary)

def projetos(request):
    context_dictionary = {'pagina': 'projetos'}
    return render(request, 'site2016/projetos.html', context_dictionary)

def exemplo_foundation(request):
    return render(request, 'site2016/ExemplosFoundation/index.html', {})