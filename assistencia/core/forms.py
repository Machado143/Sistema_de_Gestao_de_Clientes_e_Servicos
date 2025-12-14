from django import forms
from .models import OrdemServico

class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        fields = '__all__'

    def clean(self):
        cleaned = super().clean()
        status = cleaned.get("status")
        data_conclusao = cleaned.get("data_conclusao")

        if status and status.nome == "Concluída" and not data_conclusao:
            self.add_error(
                'data_conclusao',
                'Informe a data de conclusão.'
            )
