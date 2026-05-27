from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

from unfold.admin import ModelAdmin

from core.models import (
    Categoria,
    ConfiguracaoSite,
    Tecnologia,
    Projeto,
    Membro,
    Atividade,
    Etapa,
    ProcessoSeletivo
)

class StatusGrupoFilter(admin.SimpleListFilter):
    title = 'grupo'
    parameter_name = 'grupo'

    def lookups(self, request, model_admin):
        return [
            ('ativos', 'Ativos'),
            ('ex', 'Ex-membros'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'ativos':
            return queryset.exclude(
                situacao=Membro.Situacao.EX_MEMBRO
            )

        if self.value() == 'ex':
            return queryset.filter(
                situacao=Membro.Situacao.EX_MEMBRO
            )

        return queryset

admin.site.unregister(User)
admin.site.unregister(Group)

# Register your models here.

@admin.register(ConfiguracaoSite)
class ConfiguracaoSiteAdmin(ModelAdmin):
    pass

@admin.register(Group)
class CustomGroupAdmin(ModelAdmin, GroupAdmin):
    pass

@admin.register(User)
class CustomUserAdmin(ModelAdmin, UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets
    fieldsets = UserAdmin.fieldsets

    add_form = UserAdmin.add_form
    form = UserAdmin.form

@admin.register(ProcessoSeletivo)
class ProcessoSeletivoAdmin(ModelAdmin):
    pass

@admin.register(Etapa)
class EtapaAdmin(ModelAdmin):
    pass

@admin.register(Membro)
class MembroAdmin(ModelAdmin):
    ordering = ["nome"]

    list_display = ['nome', 'sobrenome', 'situacao']
    list_filter = [StatusGrupoFilter, 'situacao']

    search_fields = ['nome', 'sobrenome']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(
            request,
            queryset,
            search_term
        )

        # Filtra apenas no autocomplete
        if request.path.endswith("/autocomplete/"):
            queryset = (
                queryset
                .exclude(situacao=Membro.Situacao.EX_MEMBRO)
                .order_by("nome")
            )

        return queryset, use_distinct

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