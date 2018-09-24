from rest_framework.viewsets import ModelViewSet
from enderecos.models import Endereco
from .serializers import EnderecoSerializer

class EnderecosViewSet(ModelViewSet):
    
    serializer_class = EnderecoSerializer

    def get_queryset(self):
        return Endereco.objects.all()

