from django.shortcuts import render, redirect
from .forms import OrdemServicoForm

def criar_ordem(request):
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ordens')
    else:
        form = OrdemServicoForm()

    return render(request, 'core/form_ordem.html', {'form': form})
