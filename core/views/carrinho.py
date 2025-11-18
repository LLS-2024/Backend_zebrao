from rest_framework import viewsets
from core.models import Carrinho, ItensCarrinho
from core.serializers import CarrinhoSerializer, ItensCarrinhoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CarrinhoViewSet(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['usuario']

class ItensCarrinhoViewSet(viewsets.ModelViewSet):
    queryset = ItensCarrinho.objects.all()
    serializer_class = ItensCarrinhoSerializer