from rest_framework import serializers

from core.models.pessoa import Endereco, Pessoa, Telefone


class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = ['id', 'numero']


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'cep', 'numero', 'complemento']


class PessoaSerializer(serializers.ModelSerializer):
    telefones = TelefoneSerializer(many=True, required=False)
    enderecos = EnderecoSerializer(many=True, required=False)

    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'cpf', 'email', 'telefones', 'enderecos']
