from django import forms
from .models import OrdemServico, Cliente, Servico, Status


class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        fields = ['cliente', 'servico', 'status', 'descricao_problema', 'data_conclusao']
        widgets = {
            'descricao_problema': forms.Textarea(attrs={'rows': 4}),
            'data_conclusao': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned = super().clean()
        status = cleaned.get("status")
        data_conclusao = cleaned.get("data_conclusao")

        if status and status.nome == "Concluída" and not data_conclusao:
            self.add_error('data_conclusao', 'Informe a data de conclusão.')
        return cleaned


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone']


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'descricao', 'preco']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['nome']