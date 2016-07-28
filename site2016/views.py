from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'site2016/home.html', {'nomes': ['Marcelo', 'Thiago', 'Fernando']})