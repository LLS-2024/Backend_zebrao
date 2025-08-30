from django.db import models


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, unique=True, blank=True, null=True)
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.nome
