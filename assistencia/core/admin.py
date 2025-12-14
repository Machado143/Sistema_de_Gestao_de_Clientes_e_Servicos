from django.contrib import admin
from .models import cliente, servico, status, OrdemServico


@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'servico', 'status', 'data_abertura')
    list_filter = ('status', 'data_abertura')
    search_fields = ('cliente__nome')
