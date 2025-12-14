from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(unique=True, verbose_name="E-mail")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    descricao = models.TextField(verbose_name="Descrição")
    preco = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Preço")

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Status(models.Model):
    nome = models.CharField(max_length=30, verbose_name="Nome")

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class OrdemServico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT, verbose_name="Serviço")
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Status")
    descricao_problema = models.TextField(verbose_name="Descrição do Problema")
    data_abertura = models.DateField(auto_now_add=True, verbose_name="Data de Abertura")
    data_conclusao = models.DateField(null=True, blank=True, verbose_name="Data de Conclusão")

    class Meta:
        verbose_name = "Ordem de Serviço"
        verbose_name_plural = "Ordens de Serviço"
        ordering = ['-data_abertura']

    def __str__(self):
        return f"OS #{self.id} - {self.cliente.nome}"