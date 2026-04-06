from django.contrib import admin

from core.models import (
    Usuario,
    Categoria,
    Tecnologia,
    Projeto,
    Membro,
    Atividade,
    Etapa,
    Processo
)

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Tecnologia)
admin.site.register(Projeto)
admin.site.register(Atividade)
admin.site.register(Etapa)
admin.site.register(Processo)

@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    ordering = ["nome"]
    list_display = ('nome', 'sobrenome', 'situacao')
    search_fields = ('nome', 'sobrenome')
    list_filter = ('situacao',)