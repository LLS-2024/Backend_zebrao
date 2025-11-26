from django.db import transaction
from rest_framework import serializers

from core.models import Compra, ItensCompra


class ItensCompraSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        # usar 'produto' (não 'livro')
        return instance.produto.preco * instance.quantidade

    class Meta:
        model = ItensCompra
        fields = ('id', 'produto', 'quantidade', 'total')
        depth = 2


class CompraSerializer(serializers.ModelSerializer):
    itens = ItensCompraSerializer(many=True, read_only=True)
    usuario = serializers.CharField(source='usuario.email', read_only=True)
    status = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Compra
        fields = ('id', 'usuario', 'status', 'total', 'itens')


class ItensCompraCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ('produto', 'quantidade')


class CompraCreateUpdateSerializer(serializers.ModelSerializer):
    itens = ItensCompraCreateUpdateSerializer(many=True)

    class Meta:
        model = Compra
        fields = ('usuario', 'itens', 'status')

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        # opcional: definir usuário pelo request (se quiser evitar enviar usuario no body)
        with transaction.atomic():
            compra = Compra.objects.create(**validated_data)
            for item_data in itens_data:
                ItensCompra.objects.create(compra=compra, **item_data)
            compra.save()
        return compra

    def update(self, compra, validated_data):
        itens_data = validated_data.pop('itens', [])
        if itens_data:
            compra.itens.all().delete()
            for item_data in itens_data:
                ItensCompra.objects.create(compra=compra, **item_data)
        return super().update(compra, validated_data)
