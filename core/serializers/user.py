from rest_framework.serializers import ModelSerializer

from core.models import Endereco, Telefone, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth = 1


class TelefoneSerializer(ModelSerializer):
    class Meta:
        model = Telefone
        fields = ['id', 'numero']


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'cep', 'numero', 'complemento']
