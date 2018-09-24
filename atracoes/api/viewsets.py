from atracoes.models import Atracao
from rest_framework.viewsets import ModelViewSet
from .serializers import AtracoesSerializer


class AtracoesViewSet(ModelViewSet):
    
    serializer_class = AtracoesSerializer

    def get_queryset(self):
        return Atracao.objects.all()