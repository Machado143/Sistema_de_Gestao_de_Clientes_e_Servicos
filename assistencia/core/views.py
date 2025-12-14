from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import OrdemServico
from .forms import OrdemServicoForm
import csv
from django.http import HttpResponse

@login_required
def lista_ordens(request):
    ordens = OrdemServico.objects.select_related('cliente', 'servico', 'status').all()
    return render(request, 'core/lista_ordens.html', {'ordens': ordens})

@login_required
def criar_ordem(request):
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ordens')
    else:
        form = OrdemServicoForm()
    return render(request, 'core/form_ordem.html', {'form': form})

@login_required
def exportar_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ordens_servico.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'Cliente', 'Serviço', 'Status', 'Data Abertura', 'Data Conclusão'])
    
    ordens = OrdemServico.objects.select_related('cliente', 'servico', 'status').all()
    for ordem in ordens:
        writer.writerow([
            ordem.id,
            ordem.cliente.nome,
            ordem.servico.nome,
            ordem.status.nome,
            ordem.data_abertura,
            ordem.data_conclusao or ''
        ])
    
    return response