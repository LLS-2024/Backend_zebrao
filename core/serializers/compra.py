
from rest_framework.serializers import CharField, ModelSerializer

from core.models import Compra


class CompraSerializer(ModelSerializer):
    class Meta:
        usuario = CharField(source='usuario.email', read_only=True)
        model = Compra
        fields = '__all__'
