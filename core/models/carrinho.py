from django.db import models
from .produto import Produto
from .user import User

class Carrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='carrinhos')
    criado_em = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return sum(item.produto.preco * item.quantidade for item in self.itens.all())
    
    def __str__(self):
        return f"Carrinho de {self.usuario.email} criado em {self.criado_em}"
    
class ItensCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens')  # noqa: E112
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='+')
    quantidade = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"