from django.db.models import query
from rest_framework import serializers
from core.models import Carrinho, ItensCarrinho, User


class ItensCarrinhoSerializer(serializers.ModelSerializer):
    carrinho = serializers.PrimaryKeyRelatedField(queryset=Carrinho.objects.all())

    class Meta:
        model = ItensCarrinho
        fields = ['id', 'produto', 'quantidade', 'carrinho']

class CarrinhoSerializer(serializers.ModelSerializer):
    itens = ItensCarrinhoSerializer(many=True, read_only=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Carrinho
        fields = ['id', 'usuario', 'criado_em', 'itens', 'total']