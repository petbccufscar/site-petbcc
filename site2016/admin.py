from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Atividade)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(ProcessoSeletivo)
admin.site.register(EtapaPS)
admin.site.register(Projeto)
admin.site.register(Categoria_de_projeto)
admin.site.register(Tecnologia)