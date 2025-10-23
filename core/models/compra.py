from django.db import models

from .produto import Produto
from .user import User


class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, 'Carrinho'
        FINALIZADO = 2, 'Finalizado'
        PAGO = 3, 'Pago'
        ENTREGUE = 4, 'Entregue'

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='compras')
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)


class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itens')  # noqa: E112
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='+')
    quantidade = models.IntegerField(default=1)
