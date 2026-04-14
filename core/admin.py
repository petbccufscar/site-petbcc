from django.contrib import admin

from unfold.admin import ModelAdmin

from core.models import (
    Usuario,
    Categoria,
    Tecnologia,
    Projeto,
    Membro,
    Atividade,
    Etapa,
    ProcessoSeletivo
)

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(ModelAdmin):
    pass

@admin.register(ProcessoSeletivo)
class ProcessoSeletivoAdmin(ModelAdmin):
    pass

@admin.register(Etapa)
class EtapaAdmin(ModelAdmin):
    pass

@admin.register(Membro)
class MembroAdmin(ModelAdmin):
    ordering = ["situacao", "nome"]

    list_display = ['nome', 'sobrenome', 'situacao']
    list_filter = ['situacao',]

    search_fields = ['nome', 'sobrenome']

@admin.register(Categoria)
class CategoriaAdmin(ModelAdmin):
    search_fields = ['nome',]

@admin.register(Tecnologia)
class TecnologiaAdmin(ModelAdmin):
    search_fields = ['nome',]

@admin.register(Projeto)
class ProjetoAdmin(ModelAdmin):
    ordering = ['nome']
    search_fields =  ['nome',]
    list_filter = ["status", "categoria"]

    autocomplete_fields = ['tecnologias', 'membros',]
    
@admin.register(Atividade)
class AtividadeAdmin(ModelAdmin):
    ordering = ['-data']
    search_fields = ['titulo', 'projeto__nome']
    list_filter = ['projeto__categoria', 'projeto']

    autocomplete_fields = ['membros', 'projeto',]