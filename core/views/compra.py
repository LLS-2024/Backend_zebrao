from rest_framework.viewsets import ModelViewSet

from core.models import Compra, ItensCompra
from core.serializers import CompraCreateUpdateSerializer, CompraSerializer, ItensCompraCreateUpdateSerializer, ItensCompraSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'usuario__id']
    
    def get_serializer_class(self):
        if self.action in {'create', 'update', 'partial_update'}:
            return CompraCreateUpdateSerializer
        return CompraSerializer

    def perform_create(self, serializer):
        # Define automaticamente o usuário logado
        serializer.save(usuario=self.request.user)

class ItensCompraViewSet(ModelViewSet):
    queryset = ItensCompra.objects.all()
    serializer_class = ItensCompraSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['compra__id', 'produto__id']

    def get_serializer_class(self):
        if self.action in {'create', 'update', 'partial_update'}:
            return ItensCompraCreateUpdateSerializer
        return ItensCompraSerializer