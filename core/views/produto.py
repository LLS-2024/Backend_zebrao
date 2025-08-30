from rest_framework.viewsets import ModelViewSet

from core.models import Produto
from core.serializers import ProdutoListRetrieveSerializer, ProdutoListSerializer, ProdutoSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ProdutoListSerializer
        elif self.action == 'retrieve':
            return ProdutoListRetrieveSerializer
        return ProdutoSerializer
