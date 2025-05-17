from rest_framework import viewsets

from core.models.pessoa import Pessoa
from core.serializers.pessoa import PessoaSerializer


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
