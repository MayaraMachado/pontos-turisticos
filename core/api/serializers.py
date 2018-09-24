from core.models import PontoTuristico
from rest_framework.serializers import ModelSerializer
from enderecos.api.serializers import EnderecoSerializer
from atracoes.api.serializers import AtracoesSerializer

class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracoesSerializer(many=True)
    endereco = EnderecoSerializer()
    class Meta:
        model = PontoTuristico
        fields = (
            'id','nome', 'descricao', 'foto',
            'atracoes', 'endereco'
        )
