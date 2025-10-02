from rest_framework.viewsets import ModelViewSet

from core.models import Produto
from core.serializers import (
    ProdutoListRetrieveSerializer,
    ProdutoListSerializer,
    ProdutoSerializer,
)


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ProdutoListSerializer
        elif self.action == 'retrieve':
            return ProdutoListRetrieveSerializer
        return ProdutoSerializer

    def get_queryset(self):
        queryset = Produto.objects.all()  # noqa: E112
        categoria = self.request.query_params.get("categoria")
        categoria_id = self.request.query_params.get("categoria_id")

        if categoria:
            queryset = queryset.filter(categoria__descricao__iexact=categoria)

        if categoria_id:
            queryset = queryset.filter(categoria__id=categoria_id)

        return queryset
