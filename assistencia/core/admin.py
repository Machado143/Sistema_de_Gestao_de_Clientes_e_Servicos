from django.contrib import admin
from .models import Cliente, Servico, Status, OrdemServico


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone')
    search_fields = ('nome', 'email')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'descricao')
    search_fields = ('nome',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'servico', 'status', 'data_abertura', 'data_conclusao')
    list_filter = ('status', 'data_abertura')
    search_fields = ('cliente__nome', 'descricao_problema')
    date_hierarchy = 'data_abertura'