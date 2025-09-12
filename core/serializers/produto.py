from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Produto
from uploader.models import Image
from uploader.serializers import ImageSerializer


class ProdutoSerializer(ModelSerializer):
    imagem_attachment_key = SlugRelatedField(
        source='capa',
        queryset=Image.objects.all(),
        slug_field='attachment_key',
        required=False,
        write_only=True,
    )
    imagem = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Produto
        fields = '__all__'


class ProdutoListSerializer(ModelSerializer):
    imagem = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Produto
        fields = ('id', 'nome', 'preco', 'imagem')


class ProdutoListRetrieveSerializer(ModelSerializer):
    imagem = ImageSerializer(required=False)

    class Meta:
        model = Produto
        fields = '__all__'
        depth = 1
