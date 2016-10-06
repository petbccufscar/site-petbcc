from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'site2016/home.html', {})
    # return render(request, 'site2016/thiagoTeste.html', {'nomes': ['Marcelo', 'Thiago', 'Fernando']})

def exemplo_foundation(request):
    return render(request, 'site2016/ExemplosFoundation/index.html', {})