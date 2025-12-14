from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import OrdemServico, Cliente, Servico, Status
from .forms import OrdemServicoForm, ClienteForm, ServicoForm, StatusForm
import csv


# ========== ORDENS DE SERVIÇO ==========

@login_required
def lista_ordens(request):
    ordens = OrdemServico.objects.select_related('cliente', 'servico', 'status').all()
    
    # Filtro de busca
    busca = request.GET.get('busca')
    if busca:
        ordens = ordens.filter(
            Q(cliente__nome__icontains=busca) |
            Q(descricao_problema__icontains=busca) |
            Q(id__icontains=busca)
        )
    
    # Filtro de status
    status_filtro = request.GET.get('status')
    if status_filtro:
        ordens = ordens.filter(status_id=status_filtro)
    
    ordens = ordens.order_by('-data_abertura')
    
    # Paginação
    paginator = Paginator(ordens, 10)  # 10 ordens por página
    page = request.GET.get('page')
    
    try:
        ordens_paginadas = paginator.page(page)
    except PageNotAnInteger:
        ordens_paginadas = paginator.page(1)
    except EmptyPage:
        ordens_paginadas = paginator.page(paginator.num_pages)
    
    status_lista = Status.objects.all()
    
    return render(request, 'core/lista_ordens.html', {
        'ordens': ordens_paginadas,
        'status_lista': status_lista
    })


@login_required
def criar_ordem(request):
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ordem de serviço criada com sucesso!')
            return redirect('lista_ordens')
    else:
        form = OrdemServicoForm()
    return render(request, 'core/form_ordem.html', {'form': form, 'acao': 'Criar'})


@login_required
def editar_ordem(request, pk):
    ordem = get_object_or_404(OrdemServico, pk=pk)
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST, instance=ordem)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ordem de serviço atualizada com sucesso!')
            return redirect('lista_ordens')
    else:
        form = OrdemServicoForm(instance=ordem)
    return render(request, 'core/form_ordem.html', {'form': form, 'acao': 'Editar'})


@login_required
def excluir_ordem(request, pk):
    ordem = get_object_or_404(OrdemServico, pk=pk)
    if request.method == 'POST':
        ordem.delete()
        messages.success(request, 'Ordem de serviço excluída com sucesso!')
        return redirect('lista_ordens')
    return render(request, 'core/confirmar_exclusao.html', {
        'objeto': ordem,
        'tipo': 'Ordem de Serviço',
        'url_cancelar': 'lista_ordens'
    })


@login_required
def detalhe_ordem(request, pk):
    ordem = get_object_or_404(OrdemServico.objects.select_related('cliente', 'servico', 'status'), pk=pk)
    return render(request, 'core/detalhe_ordem.html', {'ordem': ordem})


@login_required
def exportar_csv(request):
    response = HttpResponse(content_type='text/csv; charset=utf-8-sig')
    response['Content-Disposition'] = 'attachment; filename="ordens_servico.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'Cliente', 'Email', 'Telefone', 'Serviço', 'Preço', 'Status', 'Problema', 'Data Abertura', 'Data Conclusão'])
    
    ordens = OrdemServico.objects.select_related('cliente', 'servico', 'status').all()
    for ordem in ordens:
        writer.writerow([
            ordem.id,
            ordem.cliente.nome,
            ordem.cliente.email,
            ordem.cliente.telefone,
            ordem.servico.nome,
            ordem.servico.preco,
            ordem.status.nome,
            ordem.descricao_problema,
            ordem.data_abertura.strftime('%d/%m/%Y'),
            ordem.data_conclusao.strftime('%d/%m/%Y') if ordem.data_conclusao else ''
        ])
    
    return response


# ========== CLIENTES ==========

@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all().order_by('nome')
    busca = request.GET.get('busca')
    if busca:
        clientes = clientes.filter(Q(nome__icontains=busca) | Q(email__icontains=busca))
    
    # Paginação
    paginator = Paginator(clientes, 12)  # 12 clientes por página
    page = request.GET.get('page')
    
    try:
        clientes_paginados = paginator.page(page)
    except PageNotAnInteger:
        clientes_paginados = paginator.page(1)
    except EmptyPage:
        clientes_paginados = paginator.page(paginator.num_pages)
    
    return render(request, 'core/lista_clientes.html', {'clientes': clientes_paginados})


@login_required
def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente criado com sucesso!')
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'core/form_cliente.html', {'form': form, 'acao': 'Criar'})


@login_required
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'core/form_cliente.html', {'form': form, 'acao': 'Editar'})


@login_required
def excluir_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente excluído com sucesso!')
        return redirect('lista_clientes')
    return render(request, 'core/confirmar_exclusao.html', {
        'objeto': cliente,
        'tipo': 'Cliente',
        'url_cancelar': 'lista_clientes'
    })


# ========== SERVIÇOS ==========

@login_required
def lista_servicos(request):
    servicos = Servico.objects.all().order_by('nome')
    busca = request.GET.get('busca')
    if busca:
        servicos = servicos.filter(nome__icontains=busca)
    
    # Paginação
    paginator = Paginator(servicos, 12)  # 12 serviços por página
    page = request.GET.get('page')
    
    try:
        servicos_paginados = paginator.page(page)
    except PageNotAnInteger:
        servicos_paginados = paginator.page(1)
    except EmptyPage:
        servicos_paginados = paginator.page(paginator.num_pages)
    
    return render(request, 'core/lista_servicos.html', {'servicos': servicos_paginados})


@login_required
def criar_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço criado com sucesso!')
            return redirect('lista_servicos')
    else:
        form = ServicoForm()
    return render(request, 'core/form_servico.html', {'form': form, 'acao': 'Criar'})


@login_required
def editar_servico(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço atualizado com sucesso!')
            return redirect('lista_servicos')
    else:
        form = ServicoForm(instance=servico)
    return render(request, 'core/form_servico.html', {'form': form, 'acao': 'Editar'})


@login_required
def excluir_servico(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        servico.delete()
        messages.success(request, 'Serviço excluído com sucesso!')
        return redirect('lista_servicos')
    return render(request, 'core/confirmar_exclusao.html', {
        'objeto': servico,
        'tipo': 'Serviço',
        'url_cancelar': 'lista_servicos'
    })


# ========== STATUS ==========

@login_required
def lista_status(request):
    status_lista = Status.objects.all().order_by('nome')
    
    # Paginação
    paginator = Paginator(status_lista, 12)
    page = request.GET.get('page')
    
    try:
        status_paginados = paginator.page(page)
    except PageNotAnInteger:
        status_paginados = paginator.page(1)
    except EmptyPage:
        status_paginados = paginator.page(paginator.num_pages)
    
    return render(request, 'core/lista_status.html', {'status_lista': status_paginados})


@login_required
def criar_status(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Status criado com sucesso!')
            return redirect('lista_status')
    else:
        form = StatusForm()
    return render(request, 'core/form_status.html', {'form': form, 'acao': 'Criar'})


@login_required
def editar_status(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.success(request, 'Status atualizado com sucesso!')
            return redirect('lista_status')
    else:
        form = StatusForm(instance=status)
    return render(request, 'core/form_status.html', {'form': form, 'acao': 'Editar'})


@login_required
def excluir_status(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        status.delete()
        messages.success(request, 'Status excluído com sucesso!')
        return redirect('lista_status')
    return render(request, 'core/confirmar_exclusao.html', {
        'objeto': status,
        'tipo': 'Status',
        'url_cancelar': 'lista_status'
    })