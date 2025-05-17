from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome


class Telefone(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, related_name='telefones')
    numero = models.CharField(max_length=20)

    def __str__(self):
        return self.numero


class Endereco(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT, related_name='enderecos')
    cep = models.CharField(max_length=10)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.cep} - {self.numero}"
