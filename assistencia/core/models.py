from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome

class Status(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class OrdemServico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)

    descricao_problema = models.TextField()
    data_abertura = models.DateField(auto_now_add=True)
    data_conclusao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"OS #{self.id} - {self.cliente.nome}"
